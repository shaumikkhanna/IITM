<template>
    <div class="signup-container">
      <h1>Signup</h1>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" />
      </div>
      <button @click="signup" class="btn">Submit</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import router from '../routes';
  
  export default {
    name: 'Signup',
  
    data() {
      return {
        username: '',
        email: '',
        password: '',
      };
    },
  
    methods: {
      signup() {
        console.log('Hello!');
  
        axios
          .post('http://localhost:8000/api/signup', {
            username: this.username,
            email: this.email,
            password: this.password,
          }, {
            headers: {
              'Content-type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
            },
          })
          .then(res => {
            console.log(res);
            router.push({ path: '/login/' });
          })
          .catch(err => {
            if (err.response) {
              console.log(err.response);
            }
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .signup-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
  }
  
  .form-group {
    margin-bottom: 10px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .btn {
    display: block;
    margin-top: 10px;
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .btn:hover {
    background-color: #0069d9;
  }
  </style>
  