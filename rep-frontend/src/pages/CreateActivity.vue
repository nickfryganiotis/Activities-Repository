<template>
  <q-page class = "row justify-center">
    <q-card class = "stepper q-my-lg relative-position">
    <transition
      appear
      enter-active-class = "animated fadeIn"
    >
      <q-card 
        class = "justify-center items-center flex" 
        style = "background-color: transparent; height: 100%"
        v-if = "status === 'loading' || status === 'success'"
      >
        <q-spinner size = "100px" color = "deep-purple-5" />
      </q-card>

      <q-stepper
        v-else
        bordered
        animated
        contracted
        v-model = "step"
        ref = "stepper"
        style = "background: transparent"
        color = "deep-purple-5"
      >
        <!-- Step 1 -->
        <q-step
          :name = '1'
          :done = "step > 1"
          icon = "add"
          title = "Title and description"
          active-color = "deep-purple-5"
          done-color = "teal"
        >
          <q-card 
            class = "q-my-xl" 
            style = "background-color: transparent" 
            flat
          >
            <!-- Header -->
            <q-card-section class = "flex justify-center">
              <p class = "text-h6 header"> Add a title and a description to your activity </p>
            </q-card-section>

            <!-- Content -->
            <q-card-section class = "flex justify-center">
              <!-- Title input -->
              <q-input        
                outlined
                label = "Add activity title"
                v-model = "title"
                class = "q-mb-md"
                hint = "* Required"
                style = "width: 70%; min-width: 300px;"
                :rules = "[val => val.length > 0 || 'Please insert a title']"
                lazy-rules
              >
              </q-input>

              <!-- Description input -->
              <q-input        
                outlined
                maxlength = "350"
                class = "q-mt-lg"
                hint = "* Required"
                label = "Add activity description"
                v-model = "description"
                style = "width: 70%; min-width: 300px;"
                :rules = "[val => val.length > 0 || 'Please insert a description']"
                lazy-rules
                autogrow
              >
              </q-input>
            </q-card-section>
          </q-card>
        </q-step>

        <!-- Step 2 -->
        <q-step
          :name = '2'
          :done = "step > 2"
          icon = "add"
          title = "Details about the activity"
          active-color = "deep-purple-5"
          done-color = "teal"
        >
          <div class = "my-grid justify-center q-my-xl">    
            <ActivityParameters />

            <ListSelectorStep 
              :title = "'Select the activity competences'"
              :displayed = "competences"
            />
          </div>
        </q-step>

        <!-- Step 3 -->
        <q-step
          :name = '3'
          :done = "step > 3"
          icon = "add"
          title = "Didactic strategies and special needs"
          active-color = "deep-purple-5"
          done-color = "teal"
        >
          <div class = "my-grid justify-center q-my-xl">
            <ListSelectorStep 
              :title = "'Select the didactic strategies used'"
              :displayed = "didactic"
            />
            
            <ListSelectorStep 
              :title = "'Select the special needs covered'"
              :displayed = "special"
            />
          </div>
        </q-step>

        <!-- Step 4 -->
        <q-step
          :name = '4'
          :done = "step > 4"
          icon = "add"
          title = "Learning objectives and evaluation"
          active-color = "deep-purple-5"
          done-color = "teal"
        >        
          <q-card 
            class = "q-my-xl" 
            style = "background-color: transparent" 
            flat
          >
            <!-- Header -->
            <q-card-section class = "flex justify-center">
              <p class = "text-h6 header"> Add learning objectives and evaluation </p>
            </q-card-section>

            <!-- Content -->
            <q-card-section class = "flex justify-center">
              <!-- Learning objectives input -->
              <q-input      
                outlined
                maxlength = "350"
                class = "q-mb-md"
                label = "Add learning objectives"
                hint = "* Required"
                v-model = "learningObjectives"
                style = "width: 70%; min-width: 300px;"              
                :rules = "[val => val.length > 0 || 'Please add learning objectives']"
                lazy-rules
                autogrow
              >
              </q-input>

              <!-- Evaluation input -->
              <q-input        
                outlined
                maxlength = "350"
                class = "q-mt-lg"
                label = "Add evaluation"
                hint = "* Required"
                v-model = "evaluation"
                style = "width: 70%; min-width: 300px;"              
                :rules = "[val => val.length > 0 || 'Please add learning objectives']"
                lazy-rules
                autogrow
              >
              </q-input>
            </q-card-section>
          </q-card>
        </q-step>

        <!-- Step 5 -->
        <q-step
          :name = '5'
          :done = "step > 5"
          icon = "add"
          title = "Source and materials needed"
          active-color = "deep-purple-5"
          done-color = "teal"
        >
          <q-card 
            class = "q-my-xl" 
            style = "background-color: transparent" 
            flat
          >
            <!-- Header -->
            <q-card-section class = "flex justify-center">
              <p class = "text-h6 header"> Add source and materials needed </p>
            </q-card-section>

            <!-- Content -->
            <q-card-section class = "flex justify-center">
              <!-- Source input -->
              <q-input      
                outlined
                maxlength = "350"
                class = "q-mb-md"
                label = "Add source"
                hint = "* Required"
                v-model = "source"
                style = "width: 70%; min-width: 300px;"              
                :rules = "[val => val.length > 0 || 'Please add source']"
                lazy-rules
                autogrow
              >
              </q-input>

              <!-- Materials input -->
              <q-input        
                outlined
                maxlength = "350"
                class = "q-mt-lg"
                label = "Add materials needed"
                hint = "* Required"
                v-model = "materials"
                style = "width: 70%; min-width: 300px;"              
                :rules = "[val => val.length > 0 || 'Please add materials needed']"
                lazy-rules
                autogrow
              >
              </q-input>
            </q-card-section>
          </q-card>
        </q-step>

        <template v-slot:navigation>
          <q-stepper-navigation class = "absolute-bottom">
            <q-btn 
              class = "float-right"
              @click = "() => step === 5 ? handleSubmit() : handleNextStep()" 
              color = "deep-purple-5" 
              :label = "step === 5 ? 'Finish' : 'Continue'" 
            />
            <q-btn 
              v-if = "step > 1"
              class = "float-left q-ml-sm" 
              flat color = "deep-purple-5" 
              @click = "$refs.stepper.previous()" 
              label = "Back" 
            />
          </q-stepper-navigation>
        </template>
      </q-stepper>
    </transition>
    </q-card>
  </q-page>
</template>

<script setup>
  import { ref, watch, computed, provide } from 'vue';
  import { useMutation } from 'vue-query';
  import { useRouter } from 'vue-router';

  import { useAlerts } from 'src/hooks/alerts';
  import { createActivity } from 'src/http-client/api/createActivity';

  import { competencesDefinitions } from 'src/texts/emosocio_competences';
  import { didacticStrategies } from 'src/texts/didactic_strategies';
  import { specialNeeds } from 'src/texts/special_needs';

  import ListSelectorStep from 'src/components/atoms/ListSelectorStep.vue';
  import ActivityParameters from 'src/components/atoms/ActivityParameters.vue';

  const step = ref(1);            // Variable used for the multi step form

  // * Extract data displayed in the lists from the js files
  const competences = ref(Object.keys(competencesDefinitions)
    .map(key => ({ id: key, value: false })));
  const didactic = ref(Object.keys(didacticStrategies)
    .map(key => ({ id: key, value: false })));
  const special = ref(Object.keys(specialNeeds)
    .map(key => ({ id: key, value: false })));


  // * Declare query variables
  const title = ref('');
  const description = ref('');
  const materials = ref('');
  const evaluation = ref('');
  const source = ref('');
  const learningObjectives = ref('');

  const minAge = ref('');
  const maxAge = ref('');
  const periodicity = ref('');
  const presence = ref('');
  const duration = ref('');
  const subgrouping = ref('');
  const teacherRole = ref('');

  // * Provide variables to the details children component
  provide('maxAge', maxAge);
  provide('minAge', minAge);
  provide('periodicity', periodicity);
  provide('presence', presence);
  provide('duration', duration);
  provide('subgrouping', subgrouping);
  provide('teacherRole', teacherRole);

  const alert = useAlerts();      // Provide alert function
  const router = useRouter();      // Provide router

  // * Handle form submission

  const { mutate, status } = useMutation({
    mutationFn: createActivity,
    onSuccess: () => {
      alert("Activity created successfully", "positive");
      router.push('/activities');
    }});

  const handleSubmit = () => {
    console.log("Finished");
    const final = {
      activity: {
        min_age: minAge.value,
        max_age: maxAge.value,
        periodicity: periodicity.value,
        presence: presence.value,
        duration: duration.value,
        sub_grouping: subgrouping.value,
        teacher_role: teacherRole.value,
        source: source.value,
      },
      activity_translation: {
        title: title.value,
        description: description.value,
        materials: materials.value,
        evaluation: evaluation.value,
        learning_objectives: learningObjectives.value,
      },
      activity_competences: competences.value.filter(comp => comp.value).map(comp => comp.id),
      activity_didactic_strategies: didactic.value.filter(did => did.value).map(did => did.id),
      activity_special_needs: special.value.filter(spe => spe.value).map(spe => spe.id),
    };

    mutate(final);
  };

  // * Handle form navigation

  function handleNextStep()
  {
    if (validate(step.value))
      step.value++;

    else
      alert("Please fill all required fields before continuing", "negative");
  }

  // * Validate form

  function validate(step) 
  {
    // Check that both title and description are not empty
    if (step === 1)
    {
      return (title.value.length > 0 
        && description.value.length > 0);
    }
    // One competence must be selected and all the dropdowns filled
    else if (step === 2) 
    {
      if (minAge.value === '' || maxAge.value === '' 
        || periodicity.value === '' 
        || presence.value === '' 
        || duration.value === '' 
        || subgrouping.value === '' 
        || teacherRole.value === ''
      )
        return false;
      else
        return competences.value.some(comp => comp.value);
    } 
    // One didactic strategy and one special need must be selected
    else if (step === 3) 
      return didactic.value.some(did => did.value) 
        && special.value.some(spe => spe.value);
    // Learning objectives and evaluation must be filled
    else if (step === 4)
      return learningObjectives.value.length > 0 
        && evaluation.value.length > 0;
    // Source and materials must be filled
    else if (step === 5)
      return source.value.length > 0 
        && materials.value.length > 0;
  }

</script>

<style lang = "scss" scoped>
  .header {
    color: $grey-9;
  }

  .stepper {
    font-family: "Trebuchet MS";
    background: linear-gradient($grey-2, white);
    width: 70%;
    min-height: 70vh;
    min-width: 550px;
  }

  .big-scroll {
    height: 30vh;
    width: 350px;
  }

  .small-scroll {
    height: 180px;
    width: 350px;
  }

  .my-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  }
</style>
