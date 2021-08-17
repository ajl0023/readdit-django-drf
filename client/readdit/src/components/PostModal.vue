<template>
  <div v-if="post" class="modal-wrapper" v-on:click="handleRouteHome">
    <div class="card-modal ">
      <p class="card-modal-author">
        {{ post && post.author ? post.author : "u/deleted" }}
      </p>
      <p class="modal-date ">6/15/2021</p>
      <h4 class="card-modal-title ">{{ post.title }}</h4>
      <div class="post-image-container"></div>
      <div class="no-user-comment-container  ">
        <p class="no-user-comment">Log in or sign up to leave a comment</p>
        <div class="auth-button-container">
          <button class="" @click="handleAuthModal('login')">log in</button
          ><button @click="handleAuthModal('signup')">sign up</button>
        </div>
      </div>
      <div class="card-modal-vote-container">
        <vote-container
          :voteTotal="post.voteTotal"
          :voteState="post.voteState"
        ></vote-container>
      </div>
      <h4 class="comment-section-header">Comments</h4>
    </div>
  </div>
</template>

<script>
import VoteContainer from "./VoteContainer.vue";
import { fetcher } from "../utils/fetcher";
export default {
  props: ["id"],
  components: {
    VoteContainer,
  },
  data() {
    return {
      post: null,
    };
  },
  beforeRouteEnter(to, from, next) {
    next((vm) => {
      vm.fetchPost();
    });
  },
  created() {},
  methods: {
    handleRouteHome(e) {
      if (e.target === this.$el) {
        this.$router.push("/");
      }
    },
    handleComment() {},
    fetchPost() {
      fetcher(`http://localhost:8000/posts/${this.id}`)
        .then((data) => {
          return data.json();
        })
        .then((data) => {
          this.post = data;
        });
    },
    handleAuthModal(type) {
      this.eventHub.$emit("authToggled", type);
    },
  },
};
</script>
