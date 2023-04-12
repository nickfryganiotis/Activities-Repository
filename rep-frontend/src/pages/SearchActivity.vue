<template>
  <div class="q-py-lg row q-pl-sm">
    <div class="col-4"></div>
    <div class="col-1"></div>
    <div class="col-7 text-h5 text-weight-regular q-mb-md">Activities</div>
    <div class="col-4">
      <q-card flat bordered class="my-card bg-light-blue-1">
        <q-card-section>
          <q-input outlined v-model="ph" placeholder="title" :dense="false" />
        </q-card-section>

        <q-card-section class="q-pt-none">
          <div class="row">
            <q-checkbox
              class="col"
              v-model="checkboxes['periodicallyRepeated']"
              label="periodically repeated"
            />
            <q-checkbox
              class="col"
              v-model="checkboxes['oneOffActivity']"
              label="one-off activity"
            />
          </div>
          <div class="row">
            <q-checkbox
              class="col"
              v-model="checkboxes['online']"
              label="online"
            />
            <q-checkbox
              class="col"
              v-model="checkboxes['inPerson']"
              label="in-person"
            />
          </div>
        </q-card-section>

        <q-card-section
          ><div class="text-body1 text-weight-bold">- Duration</div>
          <div class="row">
            <q-checkbox
              class="col"
              v-model="checkboxes['oneLectiveHour']"
              label="one lective hour (50 minutes)"
            />
            <q-checkbox
              class="col"
              v-model="checkboxes['threeLectiveHours']"
              label="three lective hours"
            />
          </div>
          <div class="row">
            <q-checkbox
              class="col"
              v-model="checkboxes['twoLectiveHours']"
              label="two lective hours"
            />
            <q-checkbox
              class="col"
              v-model="checkboxes['fourLectiveHours']"
              label="four lective hours"
            />
          </div>
        </q-card-section>

        <q-card-section>
          <div class="text-body1 text-weight-bold">- Age Target Group</div>
          <div class="row">
            <q-checkbox
              class="col"
              v-model="checkboxes['sixEightYears']"
              label="6-8 years"
            />
            <q-checkbox
              class="col"
              v-model="checkboxes['eightTwelveYears']"
              label="8-12 years"
            />
            <q-checkbox
              class="col"
              v-model="checkboxes['thirteenSeventenYears']"
              label="13-17 years"
            />
          </div>
        </q-card-section>

        <q-card-section>
          <div class="text-body1 text-weight-bold">+ EmoSocio competencies</div>
        </q-card-section>

        <q-card-section
          ><div class="text-body1 text-weight-bold">- Sub-grouping</div>
          <div class="row">
            <q-checkbox
              class="col"
              v-model="checkboxes['groupOfStudents']"
              label="group of students"
            />
            <q-checkbox
              class="col"
              v-model="checkboxes['individualIntervention']"
              label="individual intervention"
            />
          </div>
          <div class="row">
            <q-checkbox
              class="col"
              v-model="checkboxes['wholeClass']"
              label="whole class"
            />
          </div>
        </q-card-section>

        <q-card-section>
          <div class="text-body1 text-weight-bold">+ Teacher Role</div>
        </q-card-section>

        <q-card-section>
          <div class="text-body1 text-weight-bold">
            + Suitable for kids with disabilities
          </div>
        </q-card-section>

        <q-card-section>
          <q-select
            outlined
            v-model="available"
            :options="availableOptions"
            label="Available in"
            stack-label
          />
        </q-card-section>
      </q-card>
    </div>
    <div class="col-1"></div>
    <div class="col-6">
      <div v-for="n in counter" :key="n">
        <div class="q-pb-xl row fit q-gutter-xs q-col-gutter no-wrap">
          <div v-if="status === 'loading'">Loading...</div>
          <ActivityCard
            v-else-if="status === 'success'"
            class="col-4"
            v-for="(activity, index) in Object.values(data).slice(
              (n - 1) * 3,
              n * 3
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
            :ratingModel="ratingModel[(n - 1) * 3 + index]"
            :responses="responses[(n - 1) * 3 + index]"
            :activityCompetences="activity['activity_competences']"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import ActivityCard from "src/components/ActivityCard.vue";
import { getActivities } from "src/hooks/getActivities";
import { useQuery } from "vue-query";

export default defineComponent({
  components: {
    ActivityCard,
  },
  setup() {
    const { status, data, error } = useQuery("getActivities", getActivities, {
      refetchOnMount: false,
    });
    return {
      ph: ref(""),
      checkboxes: ref({
        periodicallyRepeated: false,
        oneOffActivity: false,
        online: false,
        inPerson: false,
        oneLectiveHour: false,
        threeLectiveHours: false,
        twoLectiveHours: false,
        fourLectiveHours: false,
        sixEightYears: false,
        eightTwelveYears: false,
        thirteenSeventenYears: false,
        groupOfStudents: false,
        individualIntervention: false,
        wholeClass: false,
      }),
      available: ref(null),
      availableOptions: ["English", "Spanish", "Romanian", "Greek"],
      counter: 6,
      ratingModel: ref([3, 1, 3, 2, 1, 4, 3, 2, 1, 3, 3, 2, 1, 3, 2, 2]),
      responses: ref([
        317, 102, 317, 205, 102, 404, 317, 205, 102, 317, 317, 205, 102, 317,
        205, 205,
      ]),
      data,
      error,
      status,
    };
  },
});
</script>
