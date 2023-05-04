<template>
  <div class = "q-pa-md" id = "parent">
    <q-card class = "q-gutter-md row items-start" id = "card-login">
      <p class = "login-font"> Please log in...</p>
      <q-form>
        <q-input
          class = "input-field"
          outlined
          v-model = "username"
          label = "Your username *"
          hint = "Username"
          lazy-rules
          :rules = "[ val => val && val.length > 0 || 'Please type something']"
        />

        <q-input 
          class = "input-field"
          outlined
          v-model = "password"  
          label = "Your password *"
          :type = "isPwd ? 'password' : 'text'" 
          hint = "Password"
          lazy-rules
          :rules = "[ 
            val => val && val.length > 0 || 'Please type something',
            val => val && val.length > 7 || 'Password must be at least 8 characters long'
          ]"
        >
          <template v-slot:append>
            <q-icon
              :name = "isPwd ? 'visibility_off' : 'visibility'"
              class = "cursor-pointer"
              @click = "isPwd = !isPwd"
            />
          </template>
        </q-input>
      </q-form>
      <q-btn 
        push 
        class = "login-button"
        color = "primary" 
        label = "Login" 
        @click = "handleLogin"
      />
    </q-card>
    
    <q-card class = "q-gutter-md row items-start" id = "card-signup">
      <p class = "signup-font"> Don't have an account? Sign up!</p>
      <q-btn 
        push 
        class = "login-button"
        color = "dark" 
        label = "SignUp" 
        @click = "handleLogin"
      />
    </q-card>
  </div>
</template>
  
<script>
  export default {
    name: 'LoginPage'
}
</script>

<script setup>
  import { ref } from 'vue'
  import axios from 'axios'

  const username = ref('');
  const password = ref('');

  const isPwd = ref(true);

  async function handleLogin()
  {
    const data = await axios.post("http://localhost:5000/login", 
    {
      username: username.value,
      password: password.value
    });

    console.log(data);
  }
</script>

<style>
  #parent {
    display: flex;
    align-items: center;
  }

  #card-login {
    padding: 0px 20px 20px 0px;
    display: grid;
    width: 30%;
    position: relative;
    top: 5%;
    left: 20%;
    min-width: 300px;
  }

  #card-signup {
    padding: 20px 20px 50px 0px;
    display: grid;
    width: 30%;
    position: relative;
    top: 5%;
    left: 30%;
    min-width: 300px;
    background: radial-gradient(circle, #35a2ff 0%, #014a88 100%);
  }

  .input-field {
    margin-bottom: 20px;
    width: 100%;
    max-width: 350px;
  }

  .login-font {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 10px;
    font-family: 'Roboto', sans-serif;
  }

  .signup-font {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 50px;
    font-family: 'Roboto', sans-serif;
    color: white;
  }

  .login-button {
    margin-top: -5px;
    min-height: 55px;
    max-width: 350px;
  }

  .card {
    position: relative;
    overflow: hidden;
    display: inline-flex;
    flex-direction: column;
    border-radius: 7px;
    box-shadow: rgba(255, 255, 255, 0.3) 0 5vw 6vw -8vw, rgba(255, 255, 255, 0) 0 4.5vw 5vw -6vw, rgba(50, 50, 80, 0.5) 0px 4vw 8vw -2vw, rgba(0, 0, 0, 0.8) 0px 4vw 5vw -3vw;
    transition: box-shadow 1s var(--cover-ease);
    width: 90vw;
    max-width: 300px;
  }
</style>

