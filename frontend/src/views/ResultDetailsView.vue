<template>
  <div>

    <HomeNavBar />
    <AccomodationHero :result="result"/>
    <div ref="homeView" class="top-24 mt-6 home-view flex flex-col items-center justify-center">
      <button @click="goBack" class="absolute top-28 left-8 w-10 h-10 bg-blue-500 text-white rounded-full shadow-md flex items-center justify-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
      </button>
      <DetailBox :result="result" />
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import DetailBox from '@/components/DetailBox.vue';
import AccomodationHero from '@/components/AccomodationHero.vue'
import HomeNavBar from '@/components/HomeNavBar.vue'

export default {
  name: 'ResultDetails',
  components: {
    Navbar,
    DetailBox,
    HomeNavBar,
    AccomodationHero,
  },
  props: ['result'], // Receive result details as props from the router
  methods: {
    goBack() {
      // Navigate back to the previous page
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped>
.home-view {
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
}
</style>
