a<template>
    <div class="home-container">
      <h1 class="title">Hello</h1>
      <div class="subtitle">This is the home page</div>
      <button class="button" @click="create" v-if="jwt">Create a blog</button>
      <button class="button" @click="myBlog" v-if="jwt">My Blogs</button>
      <h1 class="feed-title" v-if="jwt">Feed</h1>
      <div v-if="blogs.length > 0">
        <div v-for="(blog, index) in blogs" :key="index" class="blog-container">
          <a v-bind:href="'/blog/' + blog.id">
          <div>
            <img :src="blog.image_url" alt="">
            <h2 class="blog-title">{{ blog.title }}</h2>
            <p class="blog-content">{{ blog.content }}</p>
            <div class="blog-footer">
              <span class="blog-date">{{ blog.date }}</span>
            </div>
            <hr class="blog-divider">
          </div>
        </a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import router from '../routes';
  
  export default {
    name: 'Home',
    data() {
      return {
        blogs: [],
        jwt : "",
        username : "",
      }
    },
    mounted() {
      this.jwt = localStorage.getItem('jwt');

      if(!this.jwt){
        router.push({ path: '/login' })

      }
  
      axios.get(`http://localhost:8000/feed`, {
          headers: {
            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
          }
        })
        .then(res => {
          // console.log(res)
          this.blogs = res.data;
          console.log(this.blogs)
        })
        .catch(function(err) {
          if (err.response) {
            console.log(err.response)
          }
        })

        axios.get(`http://localhost:8000/check_user`, {
          headers: {
            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
          }
        })
        .then(res => {
          this.username = res.data;
          console.log(this.blogs)
        })
        .catch(function(err) {
          if (err.response) {
            console.log(err.response)
          }
        })
      
    },
    methods: {
      create() {
        router.push({ path: '/create' })
      },
      myBlog(){
        
        router.push({ path: `/user/${this.username}` })
      }
    }
  }
  </script>
  
  <style>
  .home-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .title {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .subtitle {
    font-size: 20px;
    margin-bottom: 20px;
  }
  
  .button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 20px;
  }
  
  .button:hover {
    background-color: #0069d9;
  }
  
  .feed-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .blog-container {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
  }
  
  .blog-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .blog-content {
    font-size: 16px;
    margin-bottom: 10px;
  }
  
  .blog-footer {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    margin-top: 10px;
  }
  
  .blog-date {
    color: #888;
  }
  
  .blog-divider {
    border: none;
    border-top: 1px solid #ccc;
    margin-top: 20px;
  }
  </style>
  