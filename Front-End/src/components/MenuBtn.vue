<template>
  <q-btn
    class="text-body1 text-weight-medium"
    no-caps
    stretch
    flat
    :ripple="false"
    :label="label"
  />
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "MenuBtn",
  props: {
    label: {
      type: String,
      required: true,
    },
  },
});
</script>
