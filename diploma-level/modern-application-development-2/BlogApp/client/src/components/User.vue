<template>
  <div class="profile">
    <div class="profile-header">
      <h2 class="profile-username">{{ this.$route.params.username }}</h2>
      <p class="profile-email">{{ email }}</p>
      <div class="follow-data">
        <p>Following : {{ followers }}</p>
        <p>Followers : {{ following }}</p>
      </div>
      <button @click="sendPdf(this.$route.params.username)" class="profile-follow-button follow-button">Mail me the monthly report</button>
    </div>
    <hr class="divider" />
    <div class="profile-body">
      <h3>Blogs</h3>
      <ul class="blog-list">
        <li v-for="blog in blogs" :key="blog.id" class="blog-item">
          <a v-bind:href="'/blog/' + blog.id">    
          <div class="profile-footer" v-if="same_user" >
            <button @click = 'editblog(blog.id)'>Edit</button>
            <button @click = 'deleteblog'>Delete</button>
          </div>
          <h4>{{ blog.title }}</h4>
          <p>{{ blog.content }}</p>
        </a>
        </li>
      </ul>
    </div>
    <div class="profile-footer" v-if = "!same_user">
      <button v-if="follow" @click="unfollowUser(this.$route.params.username)" class="profile-follow-button unfollow-button">Unfollow</button>
      <button v-else @click="followUser(this.$route.params.username)" class="profile-follow-button follow-button">Follow</button>
    </div>
    
  </div>
</template>

  
<script>
import router from '../routes';
  import axios from "axios";
  
  export default {
    data() {
      return {
        email: "",
        username: "",
        blogs: [],
        id:'',
        follow:null,
        user_id:'',
        jwt_username: '',
        same_user : false,
        followers : 0,
        following: 0
      };
    },
    mounted() {
      const username = this.$route.params.username;
      axios.get(`http://localhost:8000/${this.$route.params.username}`, { 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    }
          }).then((res) => {
        this.username = res.data.username;
        this.email = res.data.email;
        this.blogs = res.data.blogs;
        this.id = res.data.id;
        console.log(res.data.id)
      });

      axios.get(`http://localhost:8000/followers/${this.$route.params.username}`, { 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    }
          }).then((res) => {
            console.log(res.data.Followers)
            this.followers = res.data.Followers.length;
            this.following = res.data.Following.length;
      }); 
      axios.get(`http://localhost:8000/is_following/${this.$route.params.username}`,{ 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    }
          }).then((res)=> {
            console.log(res.data)
            this.follow = res.data
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
        console.log(res.data)
        this.jwt_username = res.data;
        if(res.data === username){
        this.same_user = true;
      }

      })
      .catch(function(err) {
        if (err.response) {
          console.log(err.response)
        }
      })
      

    },
    methods : {
        sendPdf(username){
        axios.get(`http://localhost:8000/monthly/${username}`,
        { 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    }
          }).then(res => 
                {
                    if(res.status === 200){
                      this.follow = true
                    }
              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
          },

        followUser(username) {
          axios.post(`http://localhost:8000/follow/${username}`,{},
            { 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    }
          }).then(res => 
                {
                    if(res.status === 200){
                      this.follow = true
                    }
              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        },
        unfollowUser(username){
          axios.post(`http://localhost:8000/api/unfollow/${username}`,{},
            { 
                headers: 
                    {
                    'Content-type': 'application/json',
                    'Access-Control-Allow-Origin' : '*',
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                    'Authorization' : `Bearer ${localStorage.getItem('jwt')}`
                    }
          }).then(res => 
                {
                    if(res.status === 200){
                      this.follow = false
                    }
              }
            ).catch(function(err){
                if(err.response){
                    console.log(err.response)
                }
            })
        },
        editblog(id){
            router.push({path : `/editblog/${id}`})
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

    }
  };
</script>
  
<style>
.profile {
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 16px;
  width: 100%;
}

.profile-header {
  display: flex;
  flex-direction: column;
}

.profile-username {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 8px;
}

.profile-email {
  font-size: 18px;
  margin-bottom: 16px;
}

.divider {
  border: none;
  border-top: 1px solid #eee;
  margin: 16px 0;
}

.profile-body {
  margin-top: 16px;
}

.blog-list {
  list-style: none;
  padding-left: 0;
}

.blog-item {
  margin-bottom: 16px;
}

.blog-item h4 {
  font-size: 20px;
  margin-bottom: 8px;
}

.blog-item p {
  font-size: 16px;
  margin-bottom: 0;
}

.profile-footer {
  display: flex;
  justify-content: center;
  margin-top: 16px;
}

.profile-follow-button {
  background-color: #1a73e8;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  padding: 8px 16px;
  transition: background-color 0.2s ease;
}

.profile-follow-button:hover {
  background-color: #0d47a1;
}

.unfollow-button {
  background-color: #dc3545;
}

.unfollow-button:hover {
  background-color: #c82333;
}

</style>