<template>
  <q-card flat class = "col-3 q-mr-md q-mt-lg">
    <q-list>
      <q-item 
        v-for = "item in dummy" 
        :key = "item"
      >
        <q-item-section>
          <div class = "row justify-between items-center">
            <p class = "q-ma-none" style = "font-size: 1.1em"> {{ item.label }}</p>
            <p class = "q-ma-none text-capitalize text-grey-8" caption style = "font-size: 1.1em"> {{ item.value }} </p>
          </div>

          <q-separator class = "q-mt-md"/>
        </q-item-section>
      </q-item>
    </q-list>
  </q-card>
</template>

<script setup>
  import { ref } from 'vue';


  const dummy = ref([
    {label: 'Age', value: '10-13'},
    {label: 'Periodicity', value: 'periodic'},
    {label: 'Duration', value: '1-hour'},
    {label: 'Presence', value: 'online'},
    {label: 'Teacher Role', value: 'leader'},
    {label: 'Sub-Grouping', value: 'teams'},
    {label: 'Age', value: '10-13'},
    {label: 'Prior Activity', value: '-'},
    {label: 'Next Activity', value: '-'}
  ]);
</script>