<template>
  <q-layout>
    <NavBar/>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';

  import NavBar from '../components/new-files/navigation/NavBar.vue';

  const router = useRouter();
</script>
