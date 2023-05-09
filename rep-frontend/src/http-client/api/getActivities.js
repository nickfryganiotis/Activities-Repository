import { api } from "src/http-client/coreAxios.js";

export const getActivities = () => api.get("/get_activities");

export const getActivitiesPerPage = ({ pageParam = 1 }) =>
  api.get("/get_activities_per_page?cursor=" + pageParam);
