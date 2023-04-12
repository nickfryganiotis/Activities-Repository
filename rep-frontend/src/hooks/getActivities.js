import { api } from "src/boot/coreAxios";

export const getActivities = () => api.get("/get_activities");

export const getActivity = async () => {
  //act_id = route.params.activityId;
  //console.log(act_id);

  const resp = await axios.get("http://localhost:5000/get_activity", {
    params: { activity_id: route.params.activityId },
  });
  console.log(resp);
  return resp.data;
  //.then((resp) => {
  //        return resp.data;
  //    })
  //  .catch((error) => {
  //  return error;
  //});
};
