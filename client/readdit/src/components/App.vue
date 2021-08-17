<template>
  <div>
    <navbar></navbar>
    <div class="app-wrapper">
      <router-view name="postModal"></router-view>
      <router-view name="home"></router-view>
      <auth-modal
        v-if="authModal.visible"
        v-bind:auth-type="authModal.type"
        @close-auth="closeModal"
      >
      </auth-modal>
    </div>
  </div>
</template>

<script>
import Navbar from "./Navbar.vue";
import AuthModal from "./AuthModal.vue";
export default {
  data: function() {
    return {
      authModal: {
        type: "",
        visible: false,
      },
    };
  },
  components: {
    Navbar,

    AuthModal,
  },
  created() {
    this.eventHub.$on("authToggled", (data) => {
      this.authModal.visible = !this.authModal.visible;
      this.authModal.type = data;
    });
  },
  methods: {
    closeModal: function() {
      this.authModal.visible = false;
    },
  },
};
</script>
