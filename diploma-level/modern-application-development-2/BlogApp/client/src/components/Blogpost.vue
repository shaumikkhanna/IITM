<script>
import axios from 'axios'
import router from '../routes';
import { useRoute } from 'vue-router'

export default {
    name: 'Blog',
    data(){
        return {
            title : "",
            content: "",
            id :"",
            image_url :"",
            user: "",
            author: ""
        }
    },
    mounted(){
            const route = useRoute();  
            const id = route.params.id;
            this.id = id;

            console.log("Hello!");
            axios.get(`http://localhost:8000/api/blog/${id}`, 
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
                    console.log(res.data)
                    this.title = res.data.blog.title,
                    this.content = res.data.blog.content,
                    this.image_url = res.data.blog.image_url,
                    this.author = res.data.blog.author_id
              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })

            axios.get(`http://localhost:8000/check_user`, 
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
                    this.user = res.data
              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        },
    methods: {
        
        edit(){
            router.push({path : `/editblog/${this.id}`})
        },
        deleteblog(){
            axios.delete(`http://localhost:8000/api/blog/${this.id}`, 
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
                    console.log("Delete success")
                    router.push({path : `/`})

              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        },
        exportblog(){
            axios.get(`http://localhost:8000/download/${this.id}`, 
            { 
                headers: 
                {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    },
                    responseType: 'blob',
          })
            .then(response => 
                {
                    const href = URL.createObjectURL(response.data);
    const link = document.createElement('a');
    link.href = href;
    link.setAttribute('download', 'blog.pdf'); 
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(href);

              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        },
    }
}
</script>

<template>
    <img :src="image_url" alt="">
    <h1>{{title}}</h1>
    <p>{{ content }}</p>
    <button v-if="user==author" @click = "edit">Edit</button>
    <button v-if="user==author" @click = "deleteblog">Delete</button>
    <button v-if="user==author" @click="exportblog"> Export</button>
</template>