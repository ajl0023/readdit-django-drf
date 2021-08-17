<template>
  <div class="post-wrapper">
    <div data-id="" class="card-container">
      <div class="card-content-container ">
        <p class="card-author"></p>
        <h4 class="card-title">
          <router-link :to="`${post.id}`">{{ post.title }} </router-link>
        </h4>
        <div class="vote-container">
          <vote-container
            :location="modal"
            :vote-total="post.voteTotal"
            :type="post"
            :post-id="post.id"
            :vote-state="post.voteState"
          ></vote-container>
        </div>
      </div>
      <div class="edit-del-container">
        <div class="edit-del-content">
          <button class="delete-button">
            <svg
              class="MuiSvgIcon-root del-svg"
              focusable="false"
              viewBox="0 0 24 24"
              aria-hidden="true"
            >
              <path
                d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"
              ></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VoteContainer from "./VoteContainer.vue";
export default {
  props: ["post"],
  name: "post-component",
  data() {
    return {};
  },
  components: {
    VoteContainer,
  },

  methods: {
    routeChange() {},
  },
};
</script>
