<template>
  <div class="hero-wrapper">
    <div class="parallax-bg bg-gray-700 rounded-2xl overflow-hidden mx-auto relative" style="max-width: 1565px; height: 506px; top:18px;">
      <img src="@/assets/varsity-student.jpeg" alt="Varsity Student" class="w-full h-full object-cover object-center parallax-img" />
      <div class="bg-gradient-to-r from-pink-400 to-indigo-400 opacity-30 absolute inset-0"></div>
      <div class="text-white p-6 absolute top-0 left-0 w-full h-full">
        <div class="text-center my-20 py-12 mt-8 md:mt-16">
          <h1 class="text-4xl lg:text-6xl font-semibold mb-4 max-w-auto mx-auto">Welcome!</h1>
          <p class="text-lg lg:text-xl mb-8 mx-auto">Discover comfortable and secure student accommodations near some of the most popular universities in South Africa.</p>
          <router-link to="/explore" class="text-xl absolute transform -translate-x-1/2 left-1/2 lg:text-2xl bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-6 rounded-lg transition duration-300 ease-in-out">Explore Now</router-link>
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
  

