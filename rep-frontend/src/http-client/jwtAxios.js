import axios from "axios";

function parseJwt(token) {
  try {
    const base64Url = token.split(".")[1];
    const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split("")
        .map((c) => `%${`00${c.charCodeAt(0).toString(16)}`.slice(-2)}`)
        .join("")
    );

    return JSON.parse(jsonPayload);
  } catch (_ex) {
    return null;
  }
}

const client = () => {
  const defaultOptions = {
    baseURL: process.env.VUE_APP_BASE_API_URL,
    headers: {
      "Content-Type": "application/json",
    },
  };

  // Create instance
  const instance = axios.create(defaultOptions);

  instance.interceptors.request.use(
    async (config) => {
      /** Here is a good place to check whether or not the token needs
       *  to be refreshed before proceeding to the actual request
       *  You can check if there is any time left such as >30sec from
       *  the exp (expires at) property of the jwt token.
       *  If token has expired, no need to get a 401 if you can manually refresh it
       */

      try {
        const { token } = JSON.parse(localStorage.getItem("user"));
        const { exp } = parseJwt(token);
        if (exp * 1000 > Date.now()) {
          config.headers.Authorization = `Bearer: ${token}`;
        }
      } catch (ex) {
        localStorage.removeItem("user");
      }

      return config;
    },
    (error) => Promise.reject(error)
  );

  // Add a response interceptor
  instance.interceptors.response.use(
    (response) => response.data,
    (err) => Promise.reject(err)
  );

  return instance;
};

export default client();
