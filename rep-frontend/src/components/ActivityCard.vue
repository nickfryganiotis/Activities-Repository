<template>
  <q-card class="rounded-borders">
    <q-card-section>
      <router-link
        :to="{
          name: 'ActivityDescription',
          params: { activityId: id },
        }"
      >
        <div class="text-h5">{{ title }}</div>
      </router-link>
    </q-card-section>
    <q-card-section class="q-pt-none">
      <q-rating
        :model-value="ratingModel"
        size="2em"
        :max="5"
        color="yellow"
        readonly
      />
      <div class="q-pl-xs q-pt-xs text-caption">
        {{ `${responses} responses` }}
      </div>
      <div class="q-pt-xs">
        {{ `${minAge} - ${maxAge} years old` }}
      </div>
      <div class="row q-pt-xs text-negative">
        <div
          v-for="(activityCompetence, index) in activityCompetences"
          :key="index"
          @click="getActivityDefinition($event)"
        >
          {{ `${activityCompetence},` }}
        </div>
      </div>
    </q-card-section>
    <q-dialog v-model="popup">
      <q-card>
        <q-card-section>
          <div class="q-pl-sm text-h6 bg-primary text-white">
            {{ activityName }}
          </div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          {{ activityDefinition }}
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-card>
</template>

<script>
/* used value instead of v-model as i cannot mutate it*/
import { defineComponent, ref } from "vue";
import { competencesDefinitions } from "src/texts/emosocio_competences";

export default defineComponent({
  name: "ActivityCard",
  props: {
    id: { type: Number },
    title: { type: String },
    minAge: { type: Number },
    maxAge: { type: Number },
    ratingModel: { type: Number },
    responses: { type: Number },
    activityCompetences: { type: Array },
  },

  setup(props) {
    const popup = ref(false);
    const activityName = ref("");
    const activityDefinition = ref("");
    const getActivityDefinition = (e) => {
      console.log(e.target.textContent.slice(0, -1));
      activityName.value = e.target.textContent.slice(0, -1);
      activityDefinition.value = competencesDefinitions[activityName.value];
      popup.value = true;
    };
    return { getActivityDefinition, popup, activityDefinition, activityName };
  },
});
</script>
