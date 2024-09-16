<template>
  <div class="hero-wrapper">
    <div class="parallax-bg bg-gray-700 rounded-2xl overflow-hidden mx-auto relative" style="max-width: 1565px; height: 506px; top:18px;">
      <img src="@/assets/varsity-student.jpeg" alt="Varsity Student" class="w-full h-full object-cover object-center parallax-img" />
      <div  class="bg-gradient-to-r from-pink-200 to-indigo-300 opacity-30 absolute inset-0"></div>
      <div class="text-white p-6 absolute top-0 left-0 w-full h-full">
        <div  class="text-center my-20 py-12 mt-28 md:mt-18">
          <h1 class="text-6xl text-gray-600 lg:text-7xl font-bold mb-4 max-w-auto mx-auto">Welcome!</h1>
          <p class="text-sm lg:text-sm font-bold text-black lg:text-gray-500 mb-8 mx-auto">
    Discover comfortable and secure student accommodation<br> near some of the most popular universities in South Africa.
          </p>
          <router-link to="/explore" class="text-xl absolute transform -translate-x-1/2 left-1/2 lg:text-2xl bg-indigo-500 hover:bg-blue-600 text-white font-semibold py-2 px-6 rounded-lg transition duration-300 ease-in-out">Search</router-link>
        </div>
      </div>
    </div>
  </div>
</template>



  
<script>
export default {
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      const parallaxImg = document.querySelector('.parallax-img');
      const scrolled = window.pageYOffset;
      const rate = scrolled * 0.5;
      parallaxImg.style.transform = `translate3d(0px, ${rate}px, 0px)`;
    }
  }
}
</script>

  
  <style scoped>
  /* Your scoped styles here */
  .hero-wrapper {
    width: calc(100% - 32px); /* Adjust as needed */
    margin-left: auto;
    margin-right: auto;
  }

  .parallax-bg {
    height: 506px; /* Height of the parallax container */
    position: relative;
    overflow: hidden;
  }
  
  .parallax-img {
    will-change: transform; /* Improve performance by letting the browser know which properties will change */
  }
  
  @media (max-width: 640px) {
    .hero-wrapper .bg-gray-700 {
      height: 600px; /* Adjust the height for smaller screens */
    }
  }
  </style>
  

