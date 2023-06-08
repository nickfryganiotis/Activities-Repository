import { api } from "src/http-client/coreAxios.js";

export const createActivity = async (data) => api.post("/create_activity/", data);