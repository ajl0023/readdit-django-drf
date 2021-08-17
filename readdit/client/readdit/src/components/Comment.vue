<template>
  <div style="position: relative; padding-left: 15px; padding-top: 10px;">
    <div class="thread-line-container" style="left: 0px;">
      <li class="thread-line"></li>
    </div>
    <div class="comment-vote-title-container">
      <div class="comment-vote-container">
        <VoteContainer :key="comment.id" />,
      </div>
      <div class="comment-container">
        <p class="comment-author ">admin</p>
        <div class="parent-comment ">comment</div>
        <div class="reply-button-container">
          <button class="reply-button">Reply</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import VoteContainer from "./VoteContainer.vue";
import { postsLoaded } from "./components";
import { fetcher } from "../utils/fetcher";

export default {
  props: ["comment"],
  name: "CommentContainer",

  data() {
    return {
      comments: [],
      text: "",
      replyToggle: false,
    };
  },
  components: {
    VoteContainer,
  },

  methods: {
    toggleReply: function() {
      console.log(234234);
      this.replyToggle = !this.replyToggle;
    },
    handleReply: function(e) {
      const form = new FormData(e.target.form);
      form.append("postid", this.postid);
      form.append("commentid", this.id);

      fetcher(`/comments/`, {
        method: "POST",
        body: form,
      })
        .then((data) => {})
        .then((data) => {});
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
