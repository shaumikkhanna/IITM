<template>
  <div class="container">
    <div class="layout">
      <div class="nav">
        <div class="links">
          <router-link to="/">Home</router-link>
          <router-link v-if="!user" to="/login">Login</router-link>
          <router-link v-if="!user" to="/signup">Signup</router-link>
          <button v-if="user" @click="logout">Logout</button>
          <div>
            <search-box></search-box>
          </div>
        </div>
      </div>
      <router-view />
    </div>
  </div>
</template>
<script lang="ts">
import router from './routes';
import { defineComponent, reactive, onMounted } from "vue";
import SearchBox from './components/SearchBox.vue';

export default defineComponent({
  name: "App",
  data(){
    return {
      user: false
    }
  },
  mounted(){
    this.checkUser()
  },
  methods : {
    logout(){
      localStorage.removeItem("jwt")
      console.log("Logout successfull")
      this.user = false
      router.push({path : `/login`})
    },
    checkUser(){
      const token = localStorage.getItem("jwt")
    if(token !== null) {
      this.user = true
    } else {
      this.user = false
    }
    }
  },
  components: {
    SearchBox
  },
  watch:{
    user(newValue, oldValue) {
            this.checkUser()
        }
  }
});
</script>
<style>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.logo {
  font-size: 2rem;
  font-weight: bold;
}

.links {
  display: flex;
  gap: 20px;
}

button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}

a {
  color: black;
  text-decoration: none;
}

a:hover {
  color: #4CAF50;
}

h1 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.blog-container {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 20px;
}
</style>