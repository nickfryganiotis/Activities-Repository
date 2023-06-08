<template>
  <q-page class = "filters-page">
    <div class = "grid q-pl-xl q-pr-lg">
      <h3> Activities </h3>

      <div class = "q-t-lg">
        <FiltersBarExpanded v-if = "width > 700">
          <CreateActivityPopup />
        </FiltersBarExpanded>

        <div class = "row" style = "align-items: flex-start">
          <!-- Grid with all activities -->
          <ActivitiesContainer 
            class = "col grid my-grid"
            :loading = "loading" 
            :data = "filteredData" 
          />
          <!-- Filters menu -->
          <FiltersCard
            class = "col"
            v-show = "width > 700"
            :filters = "filters"
          />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
  import { ref, provide, watch, computed } from 'vue';
  import { onMounted, onBeforeUnmount } from 'vue';
  import { useQuery, useQueryClient } from 'vue-query';

  import _ from 'lodash';
  
  import { getFilteredActivities } from 'src/http-client/api/getActivities';
  
  import { filtersDefinitions } from 'src/texts/filters';

  import FiltersCard from 'components/FiltersCard.vue';
  import ActivityCard from 'components/atoms/ActivityCard.vue'
  import ActivitiesContainer from 'components/ActivitiesContainer.vue';
  import CreateActivityPopup from 'components/CreateActivityPopup.vue';
  import FiltersBarExpanded from 'components/atoms/FiltersBarExpanded.vue'

  // * Provide variables for the input form
  const text = ref('');
  const setText = (value) => { text.value = value; };

  provide('text', text);
  provide('setText', setText);

  const filters = ref(filtersDefinitions);       // Import filters and reference them
  const filtersList = ref({});                   // Define a list of filters

  // * Watch for changes in the filters
  watch([filters, text], _.debounce(() => {
    filtersList.value = {};                      // Initialize the list

    // Foreach filter, add its selected options to the list
    filters.value.forEach(filter => {       
      filtersList.value[filter.id] = [];

      filter.options.forEach(option => {
        if (option.value == true)
          filtersList.value[filter.id].push(option.id);
      });
    })

    console.log(filtersList.value);
    filtersList.value['title'] = text.value;     // Add the input filter to the list
  
  	client.refetchQueries({ queryKey: 'filteredData' });        // Refetch the data
  }, 200), { deep: true });

  // * Function that resets filters
  function resetFilters() 
  { 
    text.value = '';                        // Reset the input form 

    // Foreach filter, reset its options
    filters.value.forEach(filter => {
      filter.options.forEach(option => {
        option.value = false;
      });
    })
  }

  provide('resetFilters', resetFilters);         // Provide function to reset filters


  const client = useQueryClient();               // Get the query client

  // * Query to get (filtered) data
  const { data: filteredData, isLoading: loading } = useQuery({
    queryKey: ['filteredData', filtersList.value],
    queryFn: () => {
      // If there are no filters, get all activities
			const empty = Object.keys(filtersList.value).length == 0 ||
				Object.values(filtersList.value).every(value => value.length == 0);

      if (empty)
        return getFilteredActivities([]);
      else
        return getFilteredActivities(filtersList.value);
    },
  })

  // TODO: Remove this in deployment
  watch(filteredData, () => { console.log(filteredData.value); });





  // * Provide variables to sort the cards
  const sorting = ref('');
  const setSorting = (value) => { sorting.value = value; };

  provide('sorting', sorting);
  provide('setSorting', setSorting);

  // * Provide variables to define the way data is displayed
  const display = ref('');
  const setDisplay = (value) => { display.value = value; };

  provide('setDisplay', setDisplay);



  // * Methods for getting the window size
  // * These are used to hide the filters card on small screens
  const width = ref(0);
  const height = ref(0);

  function getWindowSize() 
  {
    width.value = window.innerWidth;
    height.value = window.innerHeight;
  }

  onMounted(() => {
    getWindowSize();
    resetFilters();
    window.addEventListener('resize', getWindowSize);
  });

  onBeforeUnmount(() => {
    window.removeEventListener('resize', getWindowSize);
  });
</script>

<style scoped>
  .filters-page {
    background-color : #FCFFFF;
    font-family: 'Trebuchet MS';
  }

  .my-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  }

  .filter-input {
    width: 100%; 
    background-color: white; 
    font-family: 'Trebuchet MS';
  }
</style>