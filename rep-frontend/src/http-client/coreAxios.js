import { boot } from "quasar/wrappers";
import axios from "axios";

const client = () => {
  const defaultOptions = {
    // baseURL: process.env.VUE_APP_BASE_API_URL,
    baseURL: "http://localhost:5000",
    headers: {
      "Content-Type": "application/json",
    },
  };

  // Create instance
  const instance = axios.create(defaultOptions);

  // Add a response interceptor
  instance.interceptors.response.use(
    (response) => response.data,
    (err) => {
      // https://axios-http.com/docs/handling_errors
      if (err.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        // console.log(err.response.data);
        // console.log(err.response.status);
      } else if (err.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
        // http.ClientRequest in node.js
        // console.log(err.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        // console.log('Error', err.message);
      }
      // console.log(err.config);
      return Promise.reject(err);
    }
  );

  return instance;
};

// export default client();

const api = client();
const coreAxios = client();

export { axios, api, coreAxios };
