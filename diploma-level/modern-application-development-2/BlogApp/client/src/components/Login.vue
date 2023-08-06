<template>
    <div class="login-container">
      <h1 class="login-title">Login</h1>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" class="form-control" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" class="form-control" />
      </div>
      <div class="form-group">
        <button @click="login" class="login-button">Login</button>
      </div>
    </div>
  </template>


<script>
import axios from 'axios'
import router from '../routes';

export default {
    name: 'Login',
    data(){
        return {
                email:"",
                password:"",
        }
    },
    methods :{
        login(){
            console.log("logincheck")
            axios.post('http://localhost:8000/api/login',{
                email: this.email,
                password: this.password
            }, { 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    }
          })
          .then(res =>{
            console.log(res)
            localStorage.setItem('jwt' , res.data.token);
            router.push({path : '/'})
          }).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        }
    }
}
</script>


<style scoped>
.login-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login-title {
  font-size: 2rem;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

.form-control {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login-button {
  background-color: #0077cc;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1rem;
}

.login-button:hover {
  background-color: #0066b3;
}
</style>