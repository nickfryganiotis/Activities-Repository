<template>
  <q-expansion-item 
    dark
    :label = "title"
    :caption = "caption"
    header-class = "text-h6 header q-pa-md"
    class = "bg-teal expansion"
  >
    <!-- Content -->
    <q-card>
      <q-card-section class = "q-ma-none q-pa-none">
        <q-list>
          <!-- Every q-item corresponds to a checkbox -->
          <q-item 
            tag = "label" 
            v-ripple     
            v-for = "data in checkboxes"
            :key = "data"
            class = "q-py-md bg-grey-2"
          >
            <q-item-section avatar>
              <q-checkbox 
                v-model = "data.value" 
                color = "teal" 
              />
            </q-item-section>

            <!-- The label of the checkbox -->
            <q-item-section>
              <q-item-label class = "text-capitalize"> {{ data.id }} </q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </q-expansion-item>
</template>

<script setup>
  import ListSelectorStep from 'components/atoms/ListSelectorStep.vue';

  const props = defineProps({
    title: {
      type: String,
      required: true,
    },
    caption: {
      type: String,
      default: '',
    },
    checkboxes: {
      type: Array,
      required: true,
    }
  });
</script>

<style lang = "scss" scoped>
  .filter-card {
    border-radius: 5px;
  }

  .expansion:first-of-type {
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
  }

  .expansion:last-of-type {
    border-bottom-left-radius: 3px;
    border-bottom-right-radius: 3px;
  }
</style>