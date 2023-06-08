<template>
    <div>
      <!-- Loops over available activities -->
      <div 
        v-if = "loading"
        class = "justify-center items-center flex"
        style = "height: 50vh; width: 100%"
      >
        <q-spinner
          color = "deep-purple"
          :thickness = "4"
          size = "100px"
        />
      </div>

      <ActivityCard 
        v-else
        class = "col-auto"
        v-for = "activity in props.data"
        :key = "activity['activity']['id']"
        :id = "activity['activity']['id']"
        :title = "activity['activity_translations'][0]['title']"
        :competences = "activity['activity_competences']"
        :description = "activity['activity_translations'][0]['description']"
      />
    </div>
</template>

<script setup>
  import { computed, inject, watch , ref} from 'vue';

  import ActivityCard from 'components/atoms/ActivityCard.vue';

  const props = defineProps({
    data: {
      type: Array,
      required: true,
      default: () => [] ,
    },
    loading: {
      type: Boolean,
      required: true,
      default: true,
    },
  });

  console.log(props.data);

  watch(props.data, (newValue) => {
    console.log('Data changed:', newValue); 
  });

  // Variables to sort the activities
  const sorting = inject('sorting');
  watch(sorting, (newValue) => {
    console.log('Sorting type changed:', newValue); 
  });


</script>

<style scoped>
  .my-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  }
</style>