<template>
  <q-page class = "flex justify-center q-pt-lg col-grow">
    <div class = "row items-center">
      <q-card class = "q-px-lg q-py-md q-card--bordered" style="max-width: 450px">
      <q-card-section>
        <div class = "text-h4">
          {{ t('loginFormLogin') }}
        </div>
      </q-card-section>
      <q-card-section>
        <login-form />
      </q-card-section>
      <q-card-actions>
        <router-link
          to = "/recover"
          style = "padding-left:10px"
        >
          {{ t('forgotPasswordLogin') }}
        </router-link>
        <q-card-actions>
          <router-link to = "/register">
            {{ t('registerButtonLogin') }}
          </router-link>
        </q-card-actions>
      </q-card-actions>
    </q-card>
    </div>
  </q-page>
</template>

<script setup>
  import LoginForm from 'src/components/forms/LoginForm';

  const { t } = useI18n();
</script>