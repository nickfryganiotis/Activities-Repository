<template>
  <q-card 
    flat 
    class = "row no-wrap"
    style = "details-card" 
  >
    <q-tabs
      v-model = 'tab'
      vertical
      class = "text-teal q-mt-lg"
    >
      <q-tab name = "competences" label = "Competences" />
      <q-tab name = "didactic info" label = "Didactic Info" />
      <q-tab name = "special needs" label = "Special Needs" />
    </q-tabs>

    <q-separator 
      vertical 
      inset 
      class = "q-ml-md"
    />

    <!-- Panel info -->
    <q-tab-panels 
      v-model = 'tab'
      animated
      vertical
      transition-prev = 'jump-up'
      transition-next = 'jump-up'
    >
      <!-- Competences panel -->
      <q-tab-panel name = 'competences' class = "row no-wrap">
        <q-card-section class = "q-pa-none">
          <q-item-label
            header
            class = "text-h6"
          >
            Competences
          </q-item-label>

          <!-- Competences list -->
          <q-list class = "q-mt-md">
            <q-item 
              v-for = "item in data.competences" 
              :key = "item"
            >
              <q-item-section>
                <div class = "row justify-between items-center">
                  <p class = "q-ma-none text-capitalize" style = "font-size: 1.1em"> {{ item }}</p>
                </div>
                <q-separator class = "q-mt-md"/>
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>

        <q-separator vertical inset />
        
        <q-card-section class = "q-pa-none">
          <q-item-label
            header
            class = "text-h6"
          >
            What are the learning objectives?
          </q-item-label>
          
          <p> {{ data.activity_translations.learning_objectives }} </p>
        </q-card-section>

      </q-tab-panel>


      <q-tab-panel name = 'didactic info'>
        <q-item-label
          header
          class = "text-h6"
        >
          Didactic Information
        </q-item-label>

        <!-- Didactic Strategies list -->
        <q-list class = "q-mt-md">
          <q-item 
            v-for = "item in data.didactic_strategies" 
            :key = "item"
          >
            <q-item-section>
              <div class = "row justify-between items-center">
                <p class = "q-ma-none text-capitalize" style = "font-size: 1.1em"> {{ item }}</p>
              </div>
              <q-separator class = "q-mt-md"/>
            </q-item-section>
          </q-item>
        </q-list>
      </q-tab-panel>

      <q-tab-panel name = 'special needs' class = "row">
        <q-card-section class = "q-pa-none">
          <q-item-label
            header
            class = "text-h6"
          >
            Special Needs
          </q-item-label>

          <!-- Special Needs list -->
          <q-list class = "q-mt-md">
            <q-item 
              v-for = "item in data.special_needs" 
              :key = "item"
            >
              <q-item-section>
                <div class = "row justify-between items-center">
                  <p class = "q-ma-none text-capitalize" style = "font-size: 1.1em"> {{ item }}</p>
                </div>
                <q-separator class = "q-mt-md"/>
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>

        <q-separator vertical inset />

        <q-card-section class = "q-pa-none">
          <q-item-label
            header
            class = "text-h6"
          >
            Suitability
          </q-item-label>
          <div class = "row">
            <p class = "q-mt-lg q-ml-md"> Is the activity suitable for special needs? </p>
            <q-icon 
              name = "check" 
              size = "2em" 
              color = "green" 
              class = "q-mt-md q-ml-md"
              v-if = "suitable"
            />

            <q-icon 
              name = "close" 
              size = "2em" 
              color = "red" 
              class = "q-mt-md q-ml-md"
              v-else
            />
          </div>
        </q-card-section>
      </q-tab-panel>
    </q-tab-panels>
  </q-card>
</template>

<script setup>
  import { ref } from 'vue';

  const props = defineProps({
    data: {
      type: Object,
      required: true,
      default: () => {},
    },
    title: {
      type: String,
      required: true,
      default: '',
    },
  });

  const tab = ref('competences');
  const suitable = ref(true);

  console.log(props.data);
</script>

<style lang = "scss" scoped>
  .details-card {
    min-width: 300px;
    min-height: 600px;
  }
</style>