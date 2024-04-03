<template>
    <div>
      <Navbar />
      
      <div ref="homeView" class="top-24 home-view flex flex-col items-center justify-center">
        <button @click="goBack" class="absolute top-28 left-4 w-10 h-10 bg-blue-500 text-white rounded-full shadow-md flex items-center justify-center">
  <!-- Custom Back Arrow SVG icon -->
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
    <!-- Custom back arrow path -->
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
  </svg>
</button>

        <DetailBox />
      </div>
    </div>
  </template>
  
  <script>
  import Hero from '@/components/Hero.vue'
  import Navbar from '@/components/Navbar.vue'
  import FeaturedResidancesMaf from '@/components/FeaturedResidancesMaf.vue'
  import DetailBox from '@/components/DetailBox.vue'
  
  export default {
    name: 'HomeView',
    components: {
      Hero,
      Navbar,
      FeaturedResidancesMaf,
      DetailBox
    },
    mounted() {
      // Scroll to top when the component is mounted
      this.scrollToTop();
    },
    methods: {
      scrollToTop() {
        // Scroll to the top of the page
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      },
      goBack() {
        // Implement logic to go back to the previous page or route
        // For example, if you're using Vue Router, you can use router.go(-1)
        this.$router.go(-1);
      }
    }
  }
  </script>
  
  
  <style scoped>
  .home-view {
    min-height: 100vh; /* Ensure the view takes up at least the full height of the viewport */
    padding: 20px; /* Add padding as needed */
    box-sizing: border-box; /* Ensure padding is included in element's total width/height */
  }
  </style>
  