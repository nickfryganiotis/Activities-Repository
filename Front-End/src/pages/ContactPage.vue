<template>
  <div class="text-h5 q-pa-md">Name</div>

  <q-form @submit="onSubmit" @reset="onReset">
    <div class="row q-pa-md">
      <q-input
        class="q-px-lg"
        filled
        v-model="first_name"
        label="First Name"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || 'Please type something']"
      />

      <q-input
        filled
        v-model="last_name"
        label="Last Name"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || 'Please type something']"
      />
    </div>
    <div class="text-h5 q-pa-md">Email</div>

    <q-input
      class="q-px-xl"
      filled
      v-model="email"
      label="someone@example.com"
      lazy-rules
      :rules="[(val) => (val && val.length > 0) || 'Please type something']"
    />

    <div class="text-h5 q-pa-md">Description</div>

    <q-input
      class="q-px-xl max-width: 300px"
      v-model="text"
      filled
      type="textarea"
    />

    <div class="row q-pa-lg">
      <div class="col"></div>
      <q-btn class="col-1" label="Send" type="submit" color="primary" />
      <div class="col-1"></div>
    </div>
  </q-form>
</template>

<script>
import { useQuasar } from "quasar";
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "ContactPage",
  setup() {
    const $q = useQuasar();
    const first_name = ref(null);
    const last_name = ref(null);
    const email = ref(null);
    const text = ref(null);

    return {
      first_name,
      last_name,
      email,
      text,
      onSubmit() {
        if (accept.value !== true) {
          $q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "You need to accept the license and terms first",
          });
        } else {
          $q.notify({
            color: "green-4",
            textColor: "white",
            icon: "cloud_done",
            message: "Submitted",
          });
        }
      },

      onReset() {
        first_name.value = null;
        age.value = null;
        accept.value = false;
      },
    };
  },
});
</script>
