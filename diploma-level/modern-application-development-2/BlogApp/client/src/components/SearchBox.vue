<template>
    <div>
      <input type="text" v-model="searchTerm" @input="searchUsers" placeholder="Search users">
      <ul v-if="searchTerm">
        <li v-for="user in searchResults" :key="user.id">
          <a v-bind:href="'/user/' + user.username">{{ user.username }}</a>
        </li>
      </ul>
      <p v-else>No results found</p>
    </div>
  </template>
  
<script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        searchTerm: '',
        searchResults: []
      }
    },
    methods: {
      searchUsers() {
        if (this.searchTerm.length >= 2) {
          axios.get(`http://localhost:8000/search?q=${this.searchTerm}`, {
          headers: {
            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
          }
        })
            .then(response => {
                console.log(response.data)
              this.searchResults = response.data
            })
            .catch(error => {
              console.log(error)
            })
        } else {
          this.searchResults = []
        }
      }
    },
    watch : {
        searchTerm(newValue, oldValue) {
            this.searchUsers()
        }
    }
  }
</script>
  
