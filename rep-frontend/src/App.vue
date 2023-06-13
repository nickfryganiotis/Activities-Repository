<template>
  <router-view />
</template>

<script setup>
  import { useQueryProvider } from 'vue-query';
  import { QueryCache, MutationCache } from 'vue-query';

  useQueryProvider({
    defaultOptions : {
      queries : {
        retry : 0,
        refetchOnWindowFocus : false,
        refetchOnReconnect : false,
        useErrorBoundary : true
      }
    },
  });

  const queryCache = new QueryCache({
    onError : (error, query) => {
      console.debug('Error on Query:', query?.queryKey);

      debouncedHandleApiError(error);
    }
  });

  const mutationCache = new MutationCache({
    onError : (error, mutation) => {
      console.debug('Error on Mutation:', mutation?.mutationKey);

      debouncedHandleApiError(error);
    }
  });
</script>
