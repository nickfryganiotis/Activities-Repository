<template>
  <div class="col q-mt-lg q-ml-lg q-pt-lg">
    <div v-if="page <= 6" class="text-h4">
      {{ page }}/6 Create a new activity
    </div>
  </div>
  <div v-if="page == 1">
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">What is the title of the activity:</div>
      <q-input
        filled
        v-model="activity_title"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || 'Please type something']"
      />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        Give a short description of the acitivity (objectives and/or methology,
        70 words)
      </div>
      <q-input
        filled
        v-model="short_description"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || 'Please type something']"
      />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">Describe the activity in detail (500 words)</div>
      <q-input
        class="max-width: 300px"
        v-model="description"
        filled
        type="textarea"
      />
    </div>

    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        Should the activity be executed periodically? This means that the
        activity could be integrated to the routines of the classroom.
      </div>
      <q-radio v-model="periodicity" val="yes" label="Yes" />
      <div></div>
      <q-radio v-model="periodicity" val="no" label="No" />
    </div>

    <div class="row q-my-md q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2 col-12">
        What is the duration of the activity? (an activity with more than four
        hours of duration should be presented as a different activity)
      </div>
      <q-checkbox
        class="col-3"
        v-model="lective_hours.one"
        label="one lective hour (50 minutes)"
      />
      <q-checkbox
        class="col-3"
        v-model="lective_hours.four"
        label="four lective hours"
      />
      <div class="col-6"></div>
      <q-checkbox
        class="col-3"
        v-model="lective_hours.two"
        label="two lective hours"
      />
      <q-checkbox class="col-3" v-model="lective_hours.other" label="Other" />
      <div class="col-6"></div>
      <q-checkbox v-model="lective_hours.three" label="three lective hours" />
    </div>
  </div>
  <div v-else-if="page == 2">
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        What is the age target group of the activity? (put all the ages)
      </div>
      <q-checkbox v-model="target_age_group.one" label="6 - 8 years" />
      <div></div>
      <q-checkbox v-model="target_age_group.two" label="8 - 12 years" />
      <div></div>
      <q-checkbox v-model="target_age_group.three" label="13 - 17 years" />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        Can the activity be executed in person, online, or both?
      </div>
      <q-checkbox v-model="execution.inperson" label="in-person" />
      <div></div>
      <q-checkbox v-model="execution.online" label="online" />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        What types of sub-groupings does the activity support?
      </div>
      <q-checkbox
        v-model="subgrouping.individual"
        label="individual intervention"
      />
      <div></div>
      <q-checkbox v-model="subgrouping.group" label="group of students" />
      <div></div>
      <q-checkbox v-model="subgrouping.whole" label="whole class" />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        In case the activity requires the division of group in smaller groups,
        what size the of sub-grouping do you recommend? eg 3, 4, 5
      </div>
      <q-input filled v-model="recommended_subgrouping" lazy-rules />
    </div>
  </div>
  <div v-else-if="page == 3">
    <div class="row q-my-md q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2 col-12">
        Which of the following EmoSocio Competencies this activity is focused
        on?
      </div>

      <q-checkbox
        v-model="emosocio_competences['empathy']"
        label="empathy"
        class="col-3"
      />
      <q-checkbox
        v-model="emosocio_competences['self-motivation']"
        label="self-motivation"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="emosocio_competences['teamwork']"
        label="teamwork"
        class="col-3"
      />
      <q-checkbox
        v-model="emosocio_competences['optimism']"
        label="optimism"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="emosocio_competences['flexibility']"
        label="flexibility"
        class="col-3"
      />
      <q-checkbox
        v-model="emosocio_competences['self-esteem']"
        label="self-esteem"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="emosocio_competences['emotional expression']"
        label="emotional expression"
        class="col-3"
      />
      <q-checkbox
        v-model="emosocio_competences['group emotional awareness']"
        label="group emotional awareness"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="emosocio_competences['assertiveness']"
        label="assertiveness"
        class="col-3"
      />
      <q-checkbox
        v-model="emosocio_competences['group emotional regulation']"
        label="group emotional regulation"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="emosocio_competences['influence']"
        label="influence"
        class="col-3"
      />
      <q-checkbox
        v-model="
          emosocio_competences['group emotional climate (affective cohesion)']
        "
        label="group emotional climate (affective cohesion)"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="emosocio_competences['relationships']"
        label="relationships"
        class="col-3"
      />
      <q-checkbox
        v-model="emosocio_competences['social cohesion']"
        label="social cohesion"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="emosocio_competences['self-awareness']"
        label="self-awareness"
        class="col-3"
      />
      <q-checkbox
        v-model="emosocio_competences['emotional-regulation']"
        label="emotional-regulation"
        class="col-3"
      />
      <div class="col-6"></div>
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">What is the role of the teacher?</div>
      <q-checkbox
        v-model="teacher_role.participant"
        label="participant (the teacher is part of the group)"
      />
      <div></div>
      <q-checkbox
        v-model="teacher_role.observer"
        label="observer (the teacher just observes, does not interact at all with the group during the activity)"
      />
      <div></div>
      <q-checkbox
        v-model="teacher_role.organizer"
        label="organizer (the teacher guides the activity without being part of the group)"
      />
    </div>
  </div>
  <div v-else-if="page == 4">
    <div class="row q-my-md q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2 col-12">
        Is this activity suitable for kids with: The disabilities categorization
        is defined by IDEA (https://sites.ed.gov/idea/) which stands for the
        U.S. Department of Education's Individuals with Disabilities Education
        Act (IDEA)
      </div>

      <q-checkbox
        v-model="disabilities['autism']"
        label="Autism"
        class="col-3"
      />
      <q-checkbox
        v-model="disabilities['other health impairment']"
        label="Other health impairment (ex: ADHD, Epilepsy etc. )"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="disabilities['blindness and deafness']"
        label="Blindness & Deafness (have both)"
        class="col-3"
      />
      <q-checkbox
        v-model="disabilities['speech or language impairment']"
        label="Speech or language impairment"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="disabilities['emotional disturbance']"
        label="Emotional Disturbance"
        class="col-3"
      />
      <q-checkbox
        v-model="disabilities['traumatic brain injury']"
        label="Traumatic brain injury"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="disabilities['hearing impairment']"
        label="Hearing impairment"
        class="col-3"
      />
      <q-checkbox
        v-model="disabilities['deafness']"
        label="Deafness"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="disabilities['intellectual disability']"
        label="Intellectual disability"
        class="col-3"
      />
      <q-checkbox
        v-model="disabilities['visual impairment incl blindness']"
        label="Visual impairment, including blindness"
        class="col-3"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="disabilities['multiple disabilities']"
        label="Multiple disabilities"
        class="col-3"
      />
      <q-checkbox
        v-model="disabilities['specific learning disability']"
        label="Specific learning disability such as dyslexia, dyscalculia, dysgraphia and other learning issues"
        class="col-3 labeltext"
      />
      <div class="col-6"></div>
      <q-checkbox
        v-model="disabilities['orthopedic impairment']"
        label="Orthopedic impairment"
        class="col-3"
      />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">Where this activity comes from?</div>
      <q-radio v-model="activity_from" val="book" label="Book" />
      <div></div>
      <q-radio v-model="activity_from" val="publication" label="Publication" />
      <div></div>
      <q-radio v-model="activity_from" val="projects" label="Projects" />
      <div></div>
      <q-radio v-model="activity_from" val="website" label="Website" />
      <div></div>
      <q-radio
        v-model="activity_from"
        val="my_contribution"
        label="My contribution"
      />
      <div></div>
      <q-radio v-model="activity_from" val="other" label="Other" />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">Name the source of the activity.</div>
      <q-input filled v-model="activity_source" lazy-rules />
    </div>
  </div>
  <div v-else-if="page == 5">
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">Update the logo of the activity (if any).</div>
      <q-file
        style="max-width: 200px"
        v-model="filesImages"
        filled
        rounded
        multiple
        label="Choose a file"
        accept=".jpg, image/*"
      />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        Specify any material needed inorder to execute the activity (e.g. cloth,
        pictures, cards, markers)
      </div>
      <q-input filled v-model="material" lazy-rules />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        The activity is available in the following languages
      </div>
      <q-checkbox v-model="languages.english" label="English" />
      <div></div>
      <q-checkbox v-model="languages.spanish" label="Spanish" />
      <div></div>
      <q-checkbox v-model="languages.romanian" label="Romanian" />
      <div></div>
      <q-checkbox v-model="languages.greek" label="Greek" />
    </div>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        Upload any multimedia material regarding the activity
      </div>
      <q-uploader
        class="q-mt-sm"
        url="http://localhost:5000/upload"
        label="Drop files here"
        multiple
        style="max-width: 300px"
      />
    </div>
  </div>
  <div v-else-if="page == 6">
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body2">
        Indicate any useful tips or notes about the activity
      </div>
      <q-input filled v-model="notes" lazy-rules />
    </div>
  </div>
  <div v-else>
    <div class="col q-mt-lg q-ml-lg q-pt-lg q-pr-md">
      <div class="text-body1 text-weight-medium">
        Your activity was created successfully!
      </div>
    </div>
  </div>
  <div v-if="page == 1" class="row justify-end q-pr-lg q-py-md">
    <q-btn label="Next" color="primary" @click="page++" />
  </div>
  <div v-else-if="page <= 6" class="row justify-between q-px-lg q-py-md">
    <q-btn label="Previous" color="primary" @click="page--" />
    <q-btn v-if="page < 6" label="Next" color="primary" @click="page++" />
    <q-btn
      v-else-if="page == 6"
      label="Subimt"
      color="primary"
      @click="page++"
    />
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    return {
      activity_title: ref(""),
      short_description: ref(""),
      description: ref(""),
      periodicity: ref("no"),
      page: ref(1),
      lective_hours: ref({
        one: false,
        two: false,
        three: false,
        four: false,
        other: false,
      }),
      target_age_group: ref({
        one: false,
        two: false,
        three: false,
      }),
      execution: ref({
        inperson: false,
        online: false,
      }),
      subgrouping: ref({
        individual: false,
        group: false,
        whole: false,
      }),
      recommended_subgrouping: ref(""),
      emosocio_competences: ref({
        empathy: false,
        "self-motivation": false,
        teamwork: false,
        optimism: false,
        flexibility: false,
        "self-esteem": false,
        "emotional expression": false,
        "group emotional awareness": false,
        assertiveness: false,
        "group emotional regulation": false,
        influence: false,
        "group emotional climate (affective cohesion)": false,
        relationships: false,
        "social cohesion": false,
        "self-awareness": false,
        "emotional-regulation": false,
      }),
      teacher_role: ref({
        participant: false,
        observer: false,
        organizer: false,
      }),
      disabilities: ref({
        autism: false,
        "other health impairment": false,
        "blindness and deafness": false,
        "speech or language impairment": false,
        "emotional disturbance": false,
        "traumatic brain injury": false,
        "hearing impairment": false,
        deafness: false,
        "intellectual disability": false,
        "visual impairment incl blindness": false,
        "multiple disabilities": false,
        "specific learning disability": false,
        "orthopedic impairment": false,
      }),
      activity_from: ref(false),
      activity_source: ref(""),
      filesImages: ref(null),
      material: ref(""),
      languages: ref({
        english: false,
        spanish: false,
        greek: false,
        romanian: false,
      }),
      notes: ref(""),
    };
  },
});
</script>

<style lang="scss" scoped>
.labeltext {
  vertical-align: bottom;
}
</style>
