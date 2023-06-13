<template>
  <q-card flat class = "q-ml-md col-8 column justify-between">
    <q-card-section>
      <q-item-label
        header
        class = "text-h6"
      >
        <q-scroll-area class = "col-shrink" style = "min-height: 350px; height: 30vh">
          {{ data.activity_translations.description }}
        </q-scroll-area>
        </q-item-label>
    </q-card-section>

    <q-card-section class = "row-2">
      <q-separator inset />
      <q-item-label
        header
        class = "text-h6 text-weight-bold q-pb-xs"
      >
        Source:
      </q-item-label>
      <q-item-label
        header
        style = "font-size: 1.1em"
      >
        {{ data.source }}
      </q-item-label>
    </q-card-section>
  </q-card>
</template>

<script setup>
  import { defineProps } from 'vue';

  const props = defineProps({
    data: {
      type: Object,
      required: true,
      default: () => {},
    },
    loading: {
      type: Boolean,
      required: true,
      default: true,
    },
  }); 
</script>