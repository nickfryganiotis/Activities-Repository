<template>
  <div v-if="status === 'success'">
    <div class="row q-pa-lg">
      <div class="col-2"></div>

      <div class="col-5">
        <div class="text-h3 text-weight-regular">
          {{ posts["title"] }}
        </div>
      </div>
    </div>

    <div class="row q-pa-lg">
      <div class="col-2"></div>
      <div class="col-6">
        <q-card flat bordered>
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Description
            </div></q-card-section
          >
          <q-card-section
            ><div class="text-h5 text-weight regular">EmoSocio Competences</div>
            <div class="text-negative q-mt-sm">
              {{ posts["activity_competences"].join(", ") }}
            </div>
          </q-card-section>
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Periodic Execution
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Duration
            </div></q-card-section
          >
          <q-card-section
            ><div class="text-h5 text-weight regular">Age target group</div>
            <div class="q-mt-sm">
              {{
                `${posts["activity"]["min_age"]} - ${posts["activity"]["max_age"]} years old`
              }}
            </div>
          </q-card-section>
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Execution
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Teacher's Role
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Suitable for kids with
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Material(s) needed
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Available in
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Prior activity
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Next activity
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Sources
            </div></q-card-section
          >
          <q-card-section>
            <div class="text-h5 text-weight regular">
              Notes/Tips
            </div></q-card-section
          >
        </q-card>
      </div>
      <div class="col-1"></div>
      <div class="col">
        <q-rating
          :model-value="ratingModel"
          size="2em"
          :max="5"
          color="yellow"
          readonly
        />
        <div>317 responses</div>
        <p>Short description:</p>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { useQuery } from "vue-query";

export default defineComponent({
  setup() {
    //const activityId = computed(() => route.params.activityId);
    const route = useRoute();
    const {
      status,
      data: posts = [],
      error,
    } = useQuery("getActivity", async () => {
      //act_id = route.params.activityId;
      //console.log(act_id);

      const resp = await axios.get("http://localhost:5000/get_activity", {
        params: { activity_id: route.params.activityId },
      });
      console.log(resp);
      return resp.data;
      //.then((resp) => {
      //        return resp.data;
      //    })
      //  .catch((error) => {
      //  return error;
      //});
    });

    return {
      ratingModel: 3,
      //activityId,
      status,
      posts,
      error,
    };
  },
});
</script>
