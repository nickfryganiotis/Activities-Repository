<template>
  <q-header>
    <q-toolbar class = "toolbar">
      <!-- Menu redirection button -->
      <q-btn 
        flat 
        no-caps
        @click = "router.push('/')"
      >
        <!-- Logo -->
        <q-avatar>
          <img src = "src/assets/Transparent-Logo-1.webp" alt = "logo" />
        </q-avatar>
        
        <!-- Title-->
        <q-toolbar-title class = "toolbar-title">
          Educardia
        </q-toolbar-title>
      </q-btn>

      <q-tabs class = "toolbar-title" v-model = "tab" shrink align = "left">
        <q-route-tab 
          name = "home"
          label = "Educardia" 
          to = "/" 
          no-caps
        />
      </q-tabs>

      <q-space />

      <!-- Menu buttons -->
      <q-tabs v-model = "tab" shrink>
        <q-route-tab 
          name = "activities"
          label = "Activities" 
          to = "/activities" 
        />
        <q-route-tab 
          name = "information"
          label = "Information" 
          to = "/create_activity" 
        />
        <q-route-tab 
          name = "login"
          label = "Login" 
          to = "/activities" 
        />
      </q-tabs>

    </q-toolbar>
  </q-header>
</template>

<script setup>
  import { ref } from 'vue';




  const tab = ref('home');
</script>

<style lang = "scss" scoped>
  @font-face {
    font-family: Lobster;
    src: url(./Lobster/Lobster-Regular.ttf);
  }

  .toolbar {
    background: linear-gradient(to right, $teal-3, $deep-orange);
  }

  .toolbar-title {
    font-family: Lobster;
    font-size: 22px;
  }
</style>