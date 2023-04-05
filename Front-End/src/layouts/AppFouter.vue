<template>
  <q-footer reveal style="background-color: white; color: unset">
    <q-separator />
    <div
      class="row justify-between items-center"
      style="
        border-bottom: 5px solid #1976d2;
        min-height: 10vh;
        z-index: 2;
        backdrop-filter: blur(3px);
      "
    >
      <div class="col">
        <div class="row justify-start items-center q-px-lg">
          <q-img
            src="~assets/erasmusplus.png"
            style="max-width: 200px"
            class="avatar"
          >
          </q-img>
          <q-img
            src="~assets/educardiabanner.png"
            style="max-width: 100px"
            class="avatar"
          >
          </q-img>
        </div>
      </div>
      <div class="col">
        <div class="row center justify-center items-center">
          &copy; {{ new Date().getFullYear()
          }}{{ " empowerd By the Erasmus+ project" }} &nbsp;
          <a href="https://educardia.eu" target="_blank">EduCardia</a>
        </div>
      </div>
      <div class="col"></div>
    </div>
  </q-footer>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "AppFouter",
});
</script>
