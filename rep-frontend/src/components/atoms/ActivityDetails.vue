<template>
  <div>
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
          <CharacteristicsList />

          <q-separator 
            vertical 
            inset 
            class = "q-ml-md" 
          />

          <ActivityDescription />
        </q-tab-panel>
        <!-- Details tab -->
        <q-tab-panel name = "details">
          Nothing
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script setup>
  import { ref } from 'vue';

  import ActivityDescription from 'components/atoms/ActivityDescription.vue';
  import CharacteristicsList from './CharacteristicsList.vue';

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

  const tab = ref('summary');
</script>