<template>
  <div
    v-bind:class="[
      orientation === 'vertical'
        ? 'vote-container vote-vertical'
        : 'vote-container',
    ]"
  >
    <li
      type="post"
      v-bind:class="[currVoteState > 0 ? 'vote-state-active' : '']"
    >
      <UpArrow v-on:click="vote(1, postId || commentId, type)" />
    </li>
    {{ currVoteTotal }}
    <li v-bind:class="[currVoteState < 0 ? 'vote-state-active' : '']" href="">
      <DownArrow v-on:click="vote(-1, postId || commentId, type)" />
    </li>
  </div>
</template>
<script>
import UpArrow from "./../assets/images/up-arrow.svg";
import DownArrow from "./../assets/images/down-arrow.svg";
import { fetcher } from "../utils/fetcher";

export default {
  name: "VoteContainer",
  components: {
    UpArrow,
    DownArrow,
  },
  data() {
    return {
      currVoteState: this.voteState,
      currVoteTotal: this.voteTotal,
    };
  },
  props: [
    "location",
    "orientation",
    "voteTotal",
    "voteState",
    "type",
    "postId",
    "commentId",
  ],

  beforeRouteEnter(to, from, next) {
    next((vm) => vm.fetchPost());
  },

  methods: {
    vote(score, type, id) {
      if (this.location === "home") {
        return;
      }

      fetcher(`/vote`, {
        method: "PUT",
        body: JSON.stringify({
          type: this.type,
          score: score,
          [this.type === "post" ? "postid" : "commentid"]:
            this.postId || this.commentId,
        }),
      })
        .then((data) => {
          return data.json();
        })
        .then((data) => {
          this.currVoteState = data.voteState;
          this.currVoteTotal = data.voteTotal;
        });
    },
  },
};
</script>
