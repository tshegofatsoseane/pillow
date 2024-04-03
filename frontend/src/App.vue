<template >

<router-view/>
<Footer />
</template>

<script>
import HomeNavBar from './components/HomeNavBar.vue'
import Hero from './components/Hero.vue'
import Footer from './components/Footer.vue'


export default {
  components: { HomeNavBar, Hero, Footer}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body{
  margin: 0;

}
</style>
