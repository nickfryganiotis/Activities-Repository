<template>
  <div>
    <div class = 'my-div'>
        hello there...
    </div>


    <!-- Loading spinner -->
    <div 
      v-if = "loading"
      class = "justify-center items-center flex"
      style = "height: 50vh; width: 100%"
    >
      <q-spinner
        color = "deep-purple-4"
        :thickness = "4"
        size = "100px"
      />
    </div>

    <!-- Tabs -->
    <q-card v-else>
        















      <q-tabs
        v-model = "tab"
      >
          <q-tab name = "summary" label = "Summary" />
          <q-tab name = "details" label = "Details" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model = "tab" animated>
        <!-- Summary tab -->
        <q-tab-panel name = "summary" class = "row">
          <CharacteristicsList 
            :data = "characteristics"
            :loading = "loading"
          />

          <q-separator 
            vertical 
            inset 
            class = "q-ml-md" 
          />

          <ActivityDescription 
            :data = "data"
            :loading = "loading"
          />
        </q-tab-panel>
        <!-- Details tab -->
        <q-tab-panel name = "details" class = "row justify-between">
          <ActivityDetails 
            :title = "'Competences'"
            :data = "data"
          />
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script setup>
  import { ref, watch, computed } from 'vue';
  import { Screen } from 'quasar';

  import ActivityDescription from './ActivityDescription.vue';
  import CharacteristicsList from './CharacteristicsList.vue';
  import ActivityDetails from './ActivityDetails.vue';

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

  const buttonColor = computed(() => {
      return $q.screen.lt.md
        ? 'primary'
        : 'secondary'
    });

  const tab = ref('summary');

  const characteristics = computed(()=> {                // Array of objects with label and value
    console.log(props.data);

    var parameters = {};

    Object.keys(props.data).map(key => {
      // If the value is null, then display N/A
      if (props.data[key] === null)
        parameters[key] = 'None';
      else
        parameters[key] = props.data[key];
    });
    
    return parameters;
  });
</script>

<style lang = "scss" scoped>
  body.screen--xs {
    .my-div {
      background-color: $deep-purple-5;
    }
  }

    .my-div {
      background-color: $deep-orange-5;
    }
</style>