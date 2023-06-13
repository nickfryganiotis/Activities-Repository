<template>
  <q-card flat class = "col-3 q-mr-md q-mt-lg">
    <q-list>
      <q-item 
        v-for = "item in fields" 
        :key = "item"
      >
        <q-item-section>
          <div class = "row justify-between items-center">
            <p class = "q-ma-none" style = "font-size: 1.1em"> {{ item.label }}</p>
            <p class = "q-ma-none text-capitalize text-grey-8" caption style = "font-size: 1.1em"> {{ item.value }} </p>
          </div>

          <q-separator class = "q-mt-md"/>
        </q-item-section>
      </q-item>
    </q-list>
  </q-card>
</template>

<script setup>
  import { ref, computed, watch } from 'vue';

  const props = defineProps({
    data: {
      type: Object,
      required: true,
      default: () => {},
    },
    loading: {
      type: Boolean,
      required: true,
      default: true,
    },
  })

  const fields = computed(() => {
    console.log(props.data);
    return [
      { label: 'Age', value: props.data.age_target_group },
      { label: 'Periodicity', value: props.data.periodicity },
      { label: 'Duration', value: props.data.duration },
      { label: 'Presence', value: props.data.presence },
      { label: 'Teacher Role', value: props.data.teacher_role },
      { label: 'Sub-Grouping', value: props.data.sub_grouping },
      { label: 'Prior Activity', value: props.data.apriory },
      { label: 'Next Activity', value: props.data.posteriory }
    ]
  });

    console.log(fields.value);

</script>