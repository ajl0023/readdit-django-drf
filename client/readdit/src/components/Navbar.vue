<template>
  <div class="navbar-container">
    <div class="navbar-content">
      <li><a href="" class="logo">readit</a></li>
      <div class="search-bar-container">
        <input placeholder="Search" type="text" class="search-bar" /><span
          class="search-icon"
          ><img src="/static/posts/images/magnifying-glass.svg" alt=""
        /></span>
        <div class="inactive"></div>
      </div>
      <Brightness></Brightness>
      <div v-if="$store.loggedIn" class="profile-wrapper">
        <button class="navbar-profile-container">
          <div class="navbar-logo-text">
            <img
              src="/static/posts/images/reddit-default.f7d549ef.svg"
              alt=""
              class="default-profile-image"
              style="background-color: rgba(0, 0, 0, 0.1);"
            />
            <p class="navbar-profile-username"></p>
          </div>
          <img
            src="/static/posts/images/Triangle.svg"
            alt=""
            class="navbar-profile-triangle"
          />
        </button>
        <div class="inactive">
          <ul class="navbar-dropdown">
            <li>
              <button class="navbar-dropdown-options ">
                Logout
              </button>
            </li>
          </ul>
        </div>
      </div>
      <div class="auth-button-container-navbar">
        <button
          v-on:click="toggleAuthModal('login')"
          id="navbar-login-button"
          class=""
        >
          log in</button
        ><button
          id="navbar-signup-button"
          v-on:click="toggleAuthModal('signup')"
        >
          sign up
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Brightness from "../assets/images/brightness.svg";
export default {
  props: ["loggedIn"],
  name: "navbar-component",
  data() {
    console.log(Brightness, 345);
    return {};
  },
  components: {
    Brightness,
  },
  methods: {
    toggleAuthModal(type) {
      this.eventHub.$emit("authToggled", type);
    },
    close() {
      this.$emit("close-auth");
    },
  },
};
</script>
