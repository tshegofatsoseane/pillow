<template>
  <div id="app">
  
    <router-view />
    
  </div>
</template>

<script>
import HomeNavBar from './components/HomeNavBar.vue'
import Hero from './components/Hero.vue'
import newbar from './components/newbar.vue'

export default {
  components: { HomeNavBar, newbar, Hero}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
}

body {
  margin: 0;
}
</style>
