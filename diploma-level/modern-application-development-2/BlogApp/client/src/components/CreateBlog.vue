<script>
import axios from 'axios'
import router from '../routes';

export default {
    name: 'Signup',
    data(){
        return {
            title :"",
            content : "",
            image_url :""
        }
    },
    methods: {
        generate(){
            console.log("Hello!");
            axios.post('http://localhost:8000/api/create_blog', 
            {   title : this.title,
                content: this.content,
                image_url: this.image_url
            },
            { 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    }
          })
            .then(res => 
                {
                    console.log(res)
                    router.push({ path: `/`})
              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        }
    }
}
</script>

<template>
    <h1>Create Blog</h1>
    <div class="">
        <label for="">Title</label>
        <input type="text" v-model="title" />
    </div>
    <div class="">
        <label for="">content</label>
        <textarea type="text" v-model="content" />
    </div>
    <div class="">
        <label for="">image_url</label>
        <textarea type="text" v-model="image_url" />
    </div>
    <div class="">
        <button @click="generate">Create Blog</button>
    </div>

</template>


<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
  font-weight: bold;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #2196f3;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #0d8bf5;
}

</style>
