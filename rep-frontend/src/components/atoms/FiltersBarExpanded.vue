<template>
  <div>
    <div class = "row justify-between">
      <div class = "flex">

        <!-- Dropdown 'sort by' button -->
        <q-btn-dropdown 
          class = "q-mb-lg q-px-lg" 
          :label = "sort"
        >
          <q-list>
            <!-- Sort by most popular -->
            <q-item 
              clickable 
              v-close-popup
              @click = "() => { sort = 'Most Popular'; setSorting(0); }"
            >
              <q-item-section>
                <q-item-label> Most Popular </q-item-label>
              </q-item-section>
            </q-item>

            <!-- Sort by best rated -->
            <q-item 
              clickable 
              v-close-popup
              @click = "() => { sort = 'Best Rated'; setSorting(1); }"
            >
              <q-item-section>
                <q-item-label> Best Rated </q-item-label>
              </q-item-section>
            </q-item>

            <!-- Sort by most recent -->
            <q-item 
              clickable 
              v-close-popup
              @click = "() => { sort = 'Most Recent'; setSorting(2); }"
            >
              <q-item-section>
                <q-item-label> Most Recent </q-item-label>
              </q-item-section>
            </q-item>

          </q-list>
        </q-btn-dropdown>

        <!-- 'View as' toggle button -->
        <q-btn-toggle class = "q-mb-lg q-mx-lg"
          v-model = "view"
          toggle-color = "teal"
          :options = "[
            {icon: 'view_module', value: 'grid'},
            {icon: 'list', value: 'list'}
          ]"
        />
        
        <!-- Slot for extra button -->
        <slot />
      </div>        
      
      <!-- Search field -->
      <q-input 
        outlined
        style = "width: 20vw; min-width: 350px; max-width:450px"
        class = "filter-input q-pr-md q-mb-lg"
        label = "Search activity"
        v-model = "text"
        lazy
        color = "teal"
      >
        <template v-slot:prepend>
          <q-icon name = "search" />
        </template>
      </q-input>
    </div>
  </div>
</template>

<script setup>
  import { ref, inject, watch } from 'vue';

  const text = inject('text');
  const setText = inject('setText');
  watch(text, (newValue) => { setText(newValue); });

  const sort = ref('Sort by');
  const view = ref('grid');

  // Variable to define sorting
  const setSorting = inject('setSorting');
  // Variable to define display
  const setDisplay = inject('setDisplay');

  // Update display on variable change
  watch(view, (newValue) => { setDisplay(newValue); });

  function createActivity() {
    console.log('Create activity');
  }
</script>