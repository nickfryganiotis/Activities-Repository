<template>
  <div>
    <!-- Create button -->
    <q-btn 
      class = "q-py-md"
      color = "teal"
      @click = "create = true"
      icon = "add"
    />

    <!-- Popup -->
    <q-dialog v-model = "create">
      <q-card class = "q-px-md q-pt-md" style = "width: 1500px; height: 45vh;">
        <!-- Multi step form -->
        <q-stepper
          v-model = "step"
          ref = "stepper"
          color = "deep-purple"
          animated
          style = "scroll: hidden;"
        >
          <q-step
            :name = '1'
            title = "Title and description"
            icon = "add"
            :done = "step > 1"
            class = "text-h6 grid"
            style = "font-size: 1.1em"
            color = "deep-purple"
          >
            <p class = "flex justify-center q-mb-lg">
              Add a title and a description to your activity.
            </p>

            <q-input        
              outlined
              style = "width: 100%; min-width: 300px;"
              label = "Add activity title"
              v-model = "title"
            >
            </q-input>

            <q-input        
              outlined
              class = "q-mt-lg"
              style = "width: 100%; min-width: 300px;"
              label = "Add activity description"
              v-model = "description"
              autogrow
            >
            </q-input>
          </q-step>

          <q-step
            :name = '2'
            title = "Add questions"
            icon = "help"
            :done = "step > 2"
            class = "text-h6"
            style = "font-size: 1.1em; height: 25vh;"
            color = "deep-purple"
          >
            <p class = "flex justify-center q-my-lg">
              Select target age group.
            </p>

            <q-btn-toggle
              v-model="model"
              toggle-color="primary"
              flat
              :options="[
                {label: 'One', value: 'one'},
                {label: 'Two', value: 'two'},
                {label: 'Three', value: 'three'}
              ]"
            />
          </q-step>

          <template v-slot:navigation>
            <q-stepper-navigation align = "right">
              <q-btn 
                @click = "$refs.stepper.next()" 
                color = "deep-purple" 
                :label = "step === 4 ? 'Finish' : 'Continue'" 
              />
              <q-btn 
                v-if = "step > 1" 
                flat color = "deep-purple" 
                @click = "$refs.stepper.previous()" 
                label = "Back" 
                class = "q-ml-sm" 
              />
            </q-stepper-navigation>
          </template>
        </q-stepper>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup>
  import { ref } from 'vue';

  const title = ref('');
  const description = ref('');
  const create = ref(false);      // Variable to display create popup

  const toggle = ref(false);

  const step = ref(1);            // Variable used for the multi step form

  function createActivity() { create.value = true; }
</script>

<style scoped>
</style>