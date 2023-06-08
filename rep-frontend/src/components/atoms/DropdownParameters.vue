<template>
  <q-item>
    <q-item-section class = "q-mr-md">
      <q-item-label> {{ title }} </q-item-label>
      <q-item-label caption> {{ caption }} </q-item-label>
    </q-item-section>
    
    <q-btn-dropdown
      flat
      class = "q-px-sm text-capitalize"
      :label = "data === '' ? '' : data"
      :options = "options"
      color = "deep-purple-5"
      no-caps
    >
      <q-list>
        <q-item
          clickable
          v-close-popup
          v-for = "option in options"
          :key = "option"
          :label = "option"
          @click = "func(option)"
          class = "text-capitalize"
        >
          <q-item-section>
            <q-item-label> {{ option }} </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </q-item>
</template>

<script setup>
  import { ref, watch, provide } from 'vue'

  const props = defineProps({
    title: {
      type: String,
      required: true
    },
    caption: {
      type: String,
      default: ''
    },
    options: {
      type: Array,
      required: true
    },
    func: {
      type: Function,
      required: true
    },
    data: {
      type: String,
      default: ''
    }
  });

</script>