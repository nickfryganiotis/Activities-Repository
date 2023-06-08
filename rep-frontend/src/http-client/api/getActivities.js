import { api } from "src/http-client/coreAxios.js";

export const getFilteredActivities = (filter) => api.post("/filter_activities/1/en/", filter);

export const getActivitiesPerPage = ({ pageParam = 1 }) =>
  api.get("/get_activities_per_page?cursor=" + pageParam);

export const getActivityById = (id) => api.get(`/get_activity/${id}/en`);
