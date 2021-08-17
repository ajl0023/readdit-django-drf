<template>
  <div v-if="post" class="modal-wrapper" v-on:click="handleRouteHome">
    <div class="card-modal ">
      <p class="card-modal-author">
        {{ post && post.author ? post.author : "u/deleted" }}
      </p>
      <p class="modal-date ">6/15/2021</p>
      <h4 class="card-modal-title ">{{ post.title }}</h4>
      <div class="post-image-container"></div>

      <div>
        <div
          v-if="this.$store.loggedIn === false"
          class="no-user-comment-container  "
        >
          <p class="no-user-comment">Log in or sign up to leave a comment</p>
          <div class="auth-button-container">
            <button @click="handleAuthModal('login')" class="">log in</button
            ><button @click="handleAuthModal('signup')">sign up</button>
          </div>
        </div>
        <div class="new-comment-container">
          <form v-on:submit.prevent="handleComment">
            <label
              id="your_name"
              type="text"
              name="your_name"
              maxlength="100"
              required
            ></label>

            <tr>
              <th></th>
              <td>
                <textarea
                  class="new-comment"
                  name="content"
                  cols="40"
                  rows="6"
                  v-model="text"
                  id="id_content"
                ></textarea
                ><input type="hidden" name="postid" id="id_postid" />
              </td>
            </tr>
            <span class="submit-comment-container"
              ><button v-on:click="handleComment" class="submit-comment-button">
                Comment
              </button>
            </span>
          </form>
        </div>
      </div>
      <div class="card-modal-vote-container">
        <vote-container
          :orientation="'horizontal'"
          :type="'post'"
          :location="'modal'"
          :postId="post.id"
          :voteTotal="post.voteTotal"
          :voteState="post.voteState"
        ></vote-container>
      </div>
      <h4 class="comment-section-header">Comments</h4>
      <div class="main-comment-container">
        <Comment
          v-for="comment in comments"
          :key="comment.id"
          :id="comment.id"
        />
      </div>
    </div>
  </div>
</template>

<script>
import VoteContainer from "./VoteContainer.vue";
// import Comment from "./Comment.vue";
import { fetcher } from "../utils/fetcher";
export default {
  props: ["id"],
  components: {
    VoteContainer,
    Comment,
  },
  data() {
    return {
      text: "",
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
    handleComment(e, id) {
      const form = new FormData(e.submitter.form);
      form.append("postid", this.id);
      form.append("commentid", id);
      fetcher(`http://localhost:8000/comments/`, {
        method: "POST",
        body: form,
      })
        .then((data) => {
          return data.json();
        })
        .then((data) => {
          this.post = data;
        });
    },
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
