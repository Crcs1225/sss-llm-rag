import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || "SSS AI Assistant";
  next();
});

createApp(App).use(router).mount("#app");
