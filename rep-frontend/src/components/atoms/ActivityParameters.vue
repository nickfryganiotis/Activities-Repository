<template>
  <q-card 
    class = "column items-center"
    style = "background-color: transparent" 
    flat
  >
    <!-- Header -->
    <q-card-section class = "column">
      <p class = "text-h6 header q-mb-none"> Add more details about the activity </p>
      <p class = "text-caption text-grey-8"> * All the fields are required </p>
    </q-card-section>

    <!-- Content -->
    <q-card-section class = "row">
      <q-scroll-area visible class = "big-scroll">
        <q-list>
          <!-- Dropdown for age group -->
          <!-- Due to the age format, the dropdown is a bit more complex -->
          <q-item>
            <q-item-section>
              <q-item-label> Target Age </q-item-label>
              <q-item-label caption> What is the target age group? </q-item-label>
            </q-item-section>
          
            <q-btn-dropdown
              flat
              class = "q-px-sm"
              :label = "minAge === '' ? '' : minAge + '-' + maxAge"
              :options = "ageParams"
              color = "deep-purple-5"
            >
              <q-list>
                <q-item
                  clickable
                  v-close-popup
                  v-for = "option in ageParams"
                  :key = "option.label"
                  :label = "option.label"
                  @click = "() => { minAge = option.value.min; maxAge = option.value.max; }"
                >
                  <q-item-section>
                    <q-item-label> {{ option.label }} </q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </q-btn-dropdown>
          </q-item>

          <q-separator spaced inset />

          <!-- The next lines could be implemented with for loop -->

          <!-- Dropdown for periodicity -->
          <DropdownParameters 
            :title = "'Periodicity'" 
            :data = "periodicity"
            :caption = "'How periodic is the activity?'" 
            :options = "periodicityParams"
            :func = "setPeriodicity" 
          />

          <q-separator spaced inset />

          <!-- Dropdown for presence -->
          <DropdownParameters
            :title = "'Presence'"
            :data = "presence"
            :caption = "'Is physical presence required?'"
            :options = "presenceParams"
            :func = "setPresence"
          />

          <q-separator spaced inset />

          <!-- Dropdown for duration -->
          <DropdownParameters
            :title = "'Duration'"
            :data = "duration"
            :caption = "'How long does the activity last?'"
            :options = "durationParams"
            :func = "setDuration"
          />

          <q-separator spaced inset />

          <!-- Dropdown for subgrouping -->
          <DropdownParameters
            :title = "'Subgrouping'"
            :data = "subgrouping"
            :caption = "'In which way are the students grouped?'"
            :options = "subgroupingParams"
            :func = "setSubgrouping"
          />

          <q-separator spaced inset />

          <!-- Dropdown for teacher role -->
          <DropdownParameters
            :title = "'Teacher role'"
            :data = "teacherRole"
            :caption = "'What is the role of the teacher?'"
            :options = "teacherRoleParams"
            :func = "setTeacherRole"
          />
        </q-list>
      </q-scroll-area>
    </q-card-section>
  </q-card>
</template>

<script setup>
  import { ref, watch } from 'vue';
  import { inject, defineEmits } from 'vue';

  import { parameters } from 'src/texts/activity_parameters';

  import DropdownParameters from 'src/components/atoms/DropdownParameters.vue';

  // * Variables for target ages
  const minAge = inject('minAge');
  const maxAge = inject('maxAge');
  const ageParams = ref(parameters.age);

  // * Variables for activity periodicity
  const periodicity = inject('periodicity');
  const periodicityParams = ref(parameters.periodicity);
  // * Function to change periodicity
  const setPeriodicity = (value) => { periodicity.value = value };


  // * Variables for activity presence
  const presence = inject('presence');
  const presenceParams = ref(parameters.presence);
  // * Function to change presence
  const setPresence = (value) => { presence.value = value };


  // * Variables for activity duration
  const duration = inject('duration');
  const durationParams = ref(parameters.duration);
  // * Function to change duration
  const setDuration = (value) => { duration.value = value };


  // * Variable for grouping type
  const subgrouping = inject('subgrouping');
  const subgroupingParams = ref(parameters.subgrouping);
  // * Function to change subgrouping
  const setSubgrouping = (value) => { subgrouping.value = value };


  // * Variable for teacher role
  const teacherRole = inject('teacherRole');
  const teacherRoleParams = ref(parameters.teacherRole);
  // * Function to change teacher role
  const setTeacherRole = (value) => { teacherRole.value = value };
</script>

<style lang = "scss" scoped>
  .big-scroll {
    height: 35vh;
    width: 20vw;
    min-width: 350px;
  }
</style>