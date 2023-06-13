<template>
  <div class = "q-mr-xl">
    <q-card 
      v-ripple
      class = "activity-card q-mb-xl cursor-pointer q-hoverable" 
      @click = "router.push(`/activity_description/${id}`)"
    >
      <!-- Title and creator -->
      <q-card-section class = "bg-deep-orange-4" style = "white-space: normal; word-break: break-word">
        <div class = "text-h6 ellipsis text-white"> {{ title }} </div>
            
        <!-- Rating -->
        <div class = "row no-wrap items-center">
          <!-- Stars -->
          <q-rating 
            size = "1em" 
            flat
            v-model = "ratingModel" 
            :max = "5" 
            color = "deep-purple"
            readonly 
          />
          <!-- Value -->
          <span class = "text-caption text-white q-ml-sm"> 
            4.2 (551) 
          </span>

        </div>
      </q-card-section>

      <!-- Description -->
      <q-scroll-area 
        class = "q-mt-md q-pb-none q-mx-md"
        style = "height: 165px; white-space: normal; word-break: break-word"
      >
        <p> {{ description }} </p>
      </q-scroll-area>
      
      <!-- Expand button -->
      <q-card-actions class = "row justify-center q-pa-none">
        <q-btn
          color = "grey"
          flat
          style = "width: 100%"
          :icon = "expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
          @click = "expandTransition"
        />
      </q-card-actions>

      <!-- Transition to competences -->
      <q-slide-transition>
        <div v-show = "expanded" style = "background: white">
          <!-- Separator -->
          <q-separator />

          <!-- Competences -->
          <q-card-section class = "row justify-center">
            <q-btn 
              class = "q-px-sm q-py-xs q-my-xs q-mr-sm text-weight-regular my-btn" 
              color = "deep-purple" 
              no-caps
              @click.prevent = "showCompetency"
              v-for = "competency in competences"
              :key = "competency.id"
            >
              {{ competency }}
            </q-btn>
          </q-card-section>
        </div>
      </q-slide-transition>

      <!-- Popup -->
      <q-dialog v-model = "popup">
        <q-card>
          <!-- Competence name -->
          <q-card-section  class = "competence-header">
            <div class = "text-h6 text-capitalize text-white"> 
              {{ competenceName }} 
            </div>
          </q-card-section>

          <!-- Competence definition -->
          <q-card-section 
            class = "q-pt-none q-mt-lg" 
            style = "font-size: 1.1em"
          >
            {{ competenceDefinition }}
          </q-card-section>

          <q-card-actions align = "right">
            <q-btn flat label = "OK" color = "deep-purple" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-card>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue';
  import { useRouter } from 'vue-router';

  import { competencesDefinitions } from 'src/texts/emosocio_competences';

  const props = defineProps({
    id: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    competences: {
      type: Array,
      required: true,
    }
  });

  const router = useRouter();

  const expanded = ref(false);         // Whether the card is expanded or not

  // Rating variables
  const ratingModel = ref(4);
  const ratingColors = ref([ 'light-blue-3', 'light-blue-6', 'blue', 'blue-9', 'blue-10' ]);

  // Popup variables
  const popup = ref(false);
  const competenceName = ref('');
  const competenceDefinition = ref('');

  // Function to show competency popup
  function showCompetency(e) 
  {
    e.stopPropagation();               // Disable the ripple effect

    const label = e.target.innerText;  // Extract the button label
    console.log(label);

    // Get the competency data
    competenceName.value = label;
    competenceDefinition.value = competencesDefinitions[label];

    popup.value = true;                      // Open the popup
  };

  // Function to expand the card
  function expandTransition(e)
  {
    e.stopPropagation();
    expanded.value = !expanded.value;
  }

  //!! #D2F1F1
</script>

<style lang = "scss">
  .activity-card {
    border-radius: 5px; 
    width: 300px; 
    /*background: radial-gradient(circle, white 0%, $deep-purple 100%);*/
    background: $grey-2;
    display: inline-block;
    overflow: auto;
    transition: transform .2s;
  }

  .activity-card:hover {
    transform: scale(1.05);
  }

  .my-btn:hover {
    transform: scale(1.05);
  }

  .competence-header {
    background: $deep-purple;
  }
</style>
