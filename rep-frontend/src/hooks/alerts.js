import { useQuasar } from "quasar";

export const useAlerts = () => {
    const { notify } = useQuasar();

    const alert = (message, type) => {
        notify({
            message,
            color: type,
            position: "bottom",
            icon: "info",
            timeout: 3000,
        });
    };

    return alert;
}