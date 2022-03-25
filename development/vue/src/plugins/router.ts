import Vue from "vue";
import VueRouter, {RouteConfig} from "vue-router";
import Main from "@/views/Main.vue";
import NYTimes from "@/views/NYTimes.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    component: Main,
  },
  {
    path: "/nytimes",
    component: NYTimes,
  },
];

export default new VueRouter({
  routes,
});
