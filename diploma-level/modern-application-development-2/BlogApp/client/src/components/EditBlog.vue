<script>
import axios from 'axios'
import { useRoute } from 'vue-router'
import router from '../routes';

export default {
    name: 'Signup',
    data(){
        return {
            title :"",
            content : "",
            id: "",
            image_url : "",
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
                    this.image_url = res.data.blog.image_url
              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        },
    methods: {
        editblog(){
            console.log("Hello!");
            axios.put(`http://localhost:8000/api/blog/${this.id}`, 
            {   title : this.title,
                content: this.content,
                image_url : this.image_url
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
                    console.log("EDITED")
                    router.push({ path: `/blog/${this.id}`})
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
    <h1>Edit Blog</h1>
    <div class="">
        <label for="">Title</label>
        <input type="text" v-model="title" />
    </div>
    <div class="">
        <label for="">content</label>
        <textarea type="text" v-model="content" />
    </div>
    <div class="">
        <label for="">image url</label>
        <textarea type="text" v-model="image_url" />
    </div>
    <div class="">
        <button @click = "editblog">Edit Blog</button>
    </div>

</template>

