const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/HomePage.vue"),
      },
      {
        path: "/login",
        name: "Login",
        component: () => import("pages/LoginPage.vue"),
      },
      {
        path: "/activities",
        component: () => import("src/pages/ActivitiesFiltering.vue"),
      },
      {
        path: "/create_activity",
        name: "CreateActivity",
        component: () => import("pages/CreateActivity.vue"),
      },
      {
        path: "/activity_description/:activityId",
        name: "ActivityDescription",
        component: () => import("pages/ActivityOverview.vue"),
      },
      {
        path: "/contact_page",
        component: () => import("pages/ContactPage.vue"),
      },
      {
        path: "/competences",
        component: () => import("pages/CompetencesDefinitions.vue"),
      },
      {
        path: "/strategies",
        component: () => import("pages/DidacticStrategies.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
