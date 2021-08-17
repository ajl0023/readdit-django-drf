<template>
  <div class="home-wrapper">
    <div class="posts-container">
      <post
        v-for="post in posts"
        v-bind:post="post"
        :key="post.id"
      ></post>
    </div>
  </div>
</template>

<script>
import Post from "./Post.vue";
import { fetcher } from "../utils/fetcher";
export default {
  props: [],
  name: "Home",
  data() {
    return {
      posts: [],
    };
  },
  created() {
    fetcher("http://localhost:8000/posts")
      .then((data) => {
        return data.json();
      })
      .then((data) => {
        this.posts.push(...data);
      });
  },
  components: {
    Post,
  },
};
</script>
