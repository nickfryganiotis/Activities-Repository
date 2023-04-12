import { useQuery } from "vue-query";
import { api } from 'src/boot/axios'

const getActivities = () =>
  useQuery("getActivities", api.get('/get_activities').then((resp) => {
    return resp.data;
  })
  .catch((error) => {
    return error;
  }), {refetchOnMount: false});

export { getActivities }


