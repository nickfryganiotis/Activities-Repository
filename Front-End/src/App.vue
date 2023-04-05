<template>
  <router-view />
  <VueQueryDevTools />
</template>

<script>
import { defineComponent } from "vue";
import { MutationCache, QueryCache, useQueryProvider } from "vue-query";
import { VueQueryDevTools } from "vue-query/devtools";

export default defineComponent({
  name: "App",
  setup() {
    useQueryProvider({
      defaultOptions: {
        queries: {
          retry: 0,
          refetchOnWindowFocus: false,
          refetchOnReconnect: false,
          useErrorBoundary: true,
        },
      },
      queryCache: new QueryCache({
        onError: (error, query) => {
          console.debug("Error on Query:", query?.queryKey);

          debouncedHandleApiError(error);
        },
      }),
      mutationCache: new MutationCache({
        onError: (error, mutation) => {
          console.debug("Error on Mutation:", mutation?.mutationKey);
          debouncedHandleApiError(error);
        },
      }),
    });
  },
});
</script>
