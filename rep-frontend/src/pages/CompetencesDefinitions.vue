<template>
  <div style="padding-bottom: 2%">
    <div v-for="n in 5" :key="n">
      <div class="row justify-around" style="padding-top: 2%">
        <q-card
          class="col-3"
          v-for="(competence, index) in competenciesDefinitionsArray.slice(
            3 * (n - 1),
            3 * n
          )"
          :key="index"
        >
          <q-card-section>
            <div class="q-pl-sm text-h6 bg-primary text-white">
              {{ competence[0] }}
            </div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            {{ competence[1] }}
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { competenciesDefinitions } from "src/texts/emosocio_competencies.js";

export default defineComponent({
  setup() {
    const competenciesDefinitionsArray = Object.keys(competenciesDefinitions).map(
      (key) => [key, competenciesDefinitions[key]]
    );
    return { competenciesDefinitionsArray };
  },
});
</script>
