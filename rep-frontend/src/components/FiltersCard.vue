<template>
  <div class = "q-pr-md col-3" style = "width: 20vw; min-width: 350px; max-width:450px">
    <!-- Filters header -->
    <q-card flat bordered class = "bg-grey-2 filter-card shadow-1 row justify-between">
      <!-- Filters title -->
      <span class = "q-pl-md q-py-md text-h6">
        Filter Search
      </span>

      <!-- Clear button -->
      <q-card-actions class = "q-pr-md">
        <q-btn 
          flat 
          padding = "sm md"
          color = "teal"
          label = "Clear all"
          @click = "resetFilters"
          size = "1.1em"
        />
      </q-card-actions>
    </q-card>


    <q-list bordered class = "rounded-borders">
      <!-- Checkboxes -->
      <CheckboxCard
        v-for = "filter in filters"
        :title = "filter.title"
        :caption = "filter.caption"
        :checkboxes = "filter.options"
        :key = "filter.title"
      />
    </q-list>
  </div>
</template>

<script setup>
  import { inject } from 'vue';
  import CheckboxCard from 'components/CheckboxCard.vue';

  const props = defineProps({
    filters: {
      type: Array,
      required: true,
    }
  });

  console.log(props.filters);

  const resetFilters = inject('resetFilters');
</script>

<style scoped>
  .filter-card {
    border-radius: 5px;
    font-family:'Trebuchet MS'
  }
</style>