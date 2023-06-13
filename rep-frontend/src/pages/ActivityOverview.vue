<template>
  <q-page class = "summary-page">
    <div class = "grid q-pl-lg q-pr-lg">
      <div class = "row flex items-center">
        <q-btn
          rounded
          icon = "arrow_back_ios"
          class = "q-mr-md q-pl-lg"
          style = "height : 50px; width : 50px;"
          to = "/activities"
        />
        <div class = "col-auto">
          <h3 v-if = "loading"> Loading... </h3>
          <h3 v-else> {{ data.activity_translations.title }} </h3>
        </div>
      </div>

      <div class = "row">
        <ActivityInfoCard
          class = "col-9"
          :loading = "loading"
          :data = "data === undefined ? {} : data"
        />
      </div>
    </div>
  </q-page>
</template>

<script setup>
  import { ref, watch } from "vue";
  import { useQuery } from "vue-query";
  import { useRoute } from "vue-router";

  import { getActivityById } from "src/http-client/api/getActivities";

  import ActivityInfoCard from "components/atoms/ActivityInfoCard.vue";

  const route = useRoute();
  const id = route.params.activityId;

  const { data, isLoading: loading } = useQuery({
    queryKey: ["getActivityById", id],
    queryFn: () => getActivityById(id),
    refetchOnMount: false
  });

  watch(data, () => {
    console.log(data.value);
  });

</script>

<style lang = "scss" scoped>
  .summary-page {
    background-color : #FCFFFF;
    font-family: 'Trebuchet MS';
  }
</style>