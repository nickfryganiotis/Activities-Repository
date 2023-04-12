import { api } from "boot/coreAxios.js";

export const getActivities = () => api.get("/get_activities");
