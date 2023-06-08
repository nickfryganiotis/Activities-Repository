<template>
  <q-card flat class = "q-ml-md col-8 column justify-between">
    <q-card-section>
      <q-item-label
        header
        class = "text-h6"
      >
        <q-scroll-area class = "col-shrink" style = "min-height: 350px; height: 30vh">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deserunt placeat magnam amet asperiores! Nisi dolorum laudantium modi, eveniet sequi eaque est. Velit fuga in natus atque sit alias beatae cum.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio eos, laudantium magnam alias ab quasi quidem eum tempore consequuntur, nostrum molestiae nesciunt. In, nemo. Temporibus excepturi commodi quos voluptatum accusantium?
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima labore omnis soluta aspernatur praesentium, ipsa beatae dolorum perferendis tenetur debitis eligendi quia cumque quisquam! Commodi laboriosam doloribus consequatur placeat minima!
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos molestiae eius impedit atque consectetur, architecto ipsa natus laboriosam sequi expedita excepturi officia itaque tenetur voluptatum nostrum. Sed error obcaecati eos!
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Neque voluptates nisi quod. Dignissimos architecto nobis voluptatibus id tenetur, accusamus eos nulla saepe. Maiores odio nihil a. Ab nemo ipsam adipisci.
        </q-scroll-area>
        </q-item-label>
    </q-card-section>

    <q-card-section class = "row-2">
      <q-separator inset />
      <q-item-label
        header
        class = "text-h6 text-weight-bold q-pb-xs"
      >
        Source:
      </q-item-label>
      <q-item-label
        header
        style = "font-size: 1.1em"
      >
        Textbook Example Source
        </q-item-label>
    </q-card-section>
  </q-card>
</template>

<script setup>
  import { defineProps } from 'vue';

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
  }); 
</script>