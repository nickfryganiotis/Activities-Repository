<template>
  <q-card style = "background-color: transparent" flat>
    <!-- Header -->
    <q-card-section class = "flex justify-center">
      <div class = "q-ma-none column">
        <p class = "text-h6 header q-mb-none"> {{ title }} </p>
        <p class = "text-caption text-grey-8 q-ma-none "> * Choose at least one option </p>
      </div>
    </q-card-section>

    <!-- Content -->
    <q-card-section class = "flex justify-center">
      <!-- Create a checkbox for each option -->
      <q-scroll-area visible class = "big-scroll">
        <q-list separator>
          <!-- Every q-item corresponds to a checkbox -->
          <q-item 
            tag = "label" 
            v-ripple     
            v-for = "data in displayed"
            :key = "data"
            class = "q-py-sm-sm q-py-lg-md"
          >
            <q-item-section avatar>
              <q-checkbox 
                v-model = "data.value" 
                color = "deep-purple-4" 
              />
            </q-item-section>

            <!-- The label of the checkbox -->
            <q-item-section>
              <q-item-label class = "text-capitalize"> {{ data.id }} </q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-card-section>
  </q-card>
</template>

<script setup>
  import { ref } from 'vue'

  const props = defineProps({
    title: {
      type: String,
      required: true
    },
    displayed: {
      type: Array,
      required: true
    }
  });
</script>

<style lang = "scss" scoped>
  .big-scroll {
    height: 35vh;
    width: 20vw;
    min-width: 350px;
  }
</style>