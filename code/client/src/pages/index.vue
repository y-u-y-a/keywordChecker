<template>
  <div class="container-fluid">
    <h1>{{ project_name }}</h1>
    <ul class="row">
      <li class="col-3 p-5 bg-base"></li>
      <li class="col-3 p-5 bg-main"></li>
      <li class="col-3 p-5 bg-base"></li>
      <li class="col-3 p-5 bg-main"></li>
    </ul>
    <ul>
      <li v-for="(post, index) in posts" :key="index">
        <a :href="'post.url'" target="_blank">{{ index + 1 }}：{{ post.title }}</a>
      </li>
    </ul>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      project_name: process.env.PROJECT_NAME,
      posts: null
    }
  },

  created() {
    this.access();
  },

  methods: {
    async access() {
      // '/api/'='http://localhost:8000/'
      const res = await axios.get('/api/');
      let get_list = res.data;
      this.posts = get_list;
    }
  }
};
</script>
