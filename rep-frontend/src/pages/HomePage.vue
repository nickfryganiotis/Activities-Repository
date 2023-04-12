<template>
  <q-page>
    <div class="row q-pt-xl">
      <div class="col-1"></div>
      <div class="col text-h5 text-weight-regular">
        The most popular activities
      </div>
    </div>

    <q-carousel
      v-if="status === 'success'"
      v-model="slide"
      transition-prev="slide-right"
      transition-next="slide-left"
      swipeable
      animated
      control-color="primary"
      infinite
      padding
      arrows
      height="350px"
      class="shadow-2 q-mt-lg rounded-borders"
    >
      <q-carousel-slide
        v-for="n in 4"
        :key="n"
        :name="n"
        class="column no-wrap"
      >
        <div class="q-pt-md row fit q-gutter-xs q-col-gutter no-wrap">
          <div class="col-2"></div>

          <ActivityCard
            class="col-2"
            v-for="(activity, index) in getIndices(ratingModel)
              .slice((n - 1) * 4, n * 4)
              .map((indx) => Object.values(data)[indx])"
            :id="activity['activity']['id']"
            :title="
              activity['activity_translations'] !== undefined
                ? activity['activity_translations'][0]['title']
                : undefined
            "
            :minAge="activity['activity']['min_age']"
            :maxAge="activity['activity']['max_age']"
            :ratingModel="ratingModel[activity['activity']['id'] - 1]"
            :responses="responses[activity['activity']['id'] - 1]"
            :activityCompetences="activity['activity_competences']"
            :key="index"
          />

          <div class="col-2"></div>
        </div>
      </q-carousel-slide>
    </q-carousel>

    <div class="row q-pt-lg">
      <div class="col-1"></div>
      <div class="col text-h5 text-weight-regular">All activities</div>
    </div>
    <div v-for="n in counter" :key="n">
      <div class="q-pt-xl row fit q-gutter-xs q-col-gutter no-wrap">
        <div class="col-2"></div>
        <div v-if="status === 'loading'">Loading...</div>
        <ActivityCard
          v-else-if="status === 'success'"
          class="col-2"
          v-for="(activity, index) in Object.values(data).slice(
            (n - 1) * 4,
            n * 4
          )"
          :id="activity['activity']['id']"
          :title="
            activity['activity_translations'] !== undefined
              ? activity['activity_translations'][0]['title']
              : undefined
          "
          :minAge="activity['activity']['min_age']"
          :maxAge="activity['activity']['max_age']"
          :key="index"
          :ratingModel="ratingModel[(n - 1) * 4 + index]"
          :responses="responses[(n - 1) * 4 + index]"
          :activityCompetences="activity['activity_competences']"
        />
        <div class="col-2"></div>
      </div>
    </div>

    <div class="row justify-center q-pr-lg q-py-md">
      <q-btn
        rounded
        push
        v-if="status === 'success'"
        color="primary"
        icon="more_horiz"
        label="Show more"
        @click="
          counter =
            counter * 4 < Object.values(data).length ? counter + 1 : counter
        "
      ></q-btn>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import ActivityCard from "src/components/ActivityCard.vue";
import { useRouter, useRoute } from "vue-router";
import { getActivities } from "src/hooks/getActivities";
import { useQuery } from "vue-query";

export default defineComponent({
  name: "IndexPage",
  components: { ActivityCard },

  setup() {
    const { push } = useRouter();
    const route = useRoute();
    const goToActivityDescription = (title) => {
      push({ path: "/activity_description", props: { title: title } });
    };

    function getIndices(ratingModel) {
      let indices = [...Array(ratingModel.length).keys()];
      indices.sort(function (u, v) {
        return ratingModel[u] > ratingModel[v]
          ? -1
          : ratingModel[u] < ratingModel[v]
          ? 1
          : 0;
      });
      return indices;
    }

    const { status, data, error } = useQuery("getActivities", getActivities, {
      refetchOnMount: false,
    });

    return {
      slide: ref(1),
      showMore: ref(false),
      counter: ref(1),
      ratingModel: ref([2, 1, 2, 2, 1, 4, 3, 2, 1, 3, 3, 2, 1, 3, 2, 2]),
      responses: ref([
        205, 102, 205, 205, 102, 404, 317, 205, 102, 317, 317, 205, 102, 317,
        205, 205,
      ]),
      getIndices,
      route,
      goToActivityDescription,
      status,
      error,
      data,
    };
  },
});
</script>
