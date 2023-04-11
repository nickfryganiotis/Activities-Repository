<template>
  <div style="padding-bottom: 2%">
    <div v-for="n in 4" :key="n">
      <div class="row justify-around" style="padding-top: 2%">
        <q-card
          class="col-3"
          v-for="(strategy, index) in didacticStrategiesArray.slice(
            3 * (n - 1),
            3 * n
          )"
          :key="index"
        >
          <q-card-section>
            <div class="q-pl-sm text-h6 bg-primary text-white">
              {{ strategy[0] }}
            </div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            {{ strategy[1] }}
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { didacticStrategies } from "src/texts/didactic_strategies.js";

export default defineComponent({
  setup() {
    const didacticStrategiesArray = Object.keys(didacticStrategies).map(
      (key) => [key, didacticStrategies[key]]
    );
    return { didacticStrategiesArray };
  },
});
</script>
