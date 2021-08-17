import VueRouter from "vue-router";
import Navbar from "./components/Navbar.vue";
import Home from "./components/Home.vue";
import AuthModal from "./components/AuthModal.vue";
import PostModal from "./components/PostModal.vue";
console.log(34);
import App from "./components/App.vue";
import Vue from "vue";

import "./eventbus";
import "./assets/css/main.css";

const store = Vue.observable({ loggedIn: false, user: null });
Vue.prototype.$store = store;
Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",

  routes: [
    {
      path: "/:id",

      components: {
        postModal: PostModal,
      },
      props: {
        postModal: (route) => {
          return { id: route.params.id };
        },
      },

      // postModal: AsyncComponent().component,
    },
    {
      path: "/",

      components: {
        home: Home,
      },
    },
  ],
});

new Vue({
  el: "#app",
  router,
  render: (h) => h(App),
  components: {
    Navbar,
    Home,
    PostModal,
    AuthModal,
  },
  created: function() {
    this.eventHub.$on("authToggled", (data) => {
      this.authModal.visible = !this.authModal.visible;
      this.authModal.type = data;
    });
  },
  data: function() {
    return {
      authModal: {
        type: "",
        visible: false,
      },
    };
  },
  methods: {
    closeModal: function() {
      this.authModal.visible = false;
    },
  },
});
