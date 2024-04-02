<template>
    <div>
      <!-- Conditional rendering based on the showSkeleton data property -->
      <template v-if="showSkeleton">
        <!-- Skeleton Template -->
        <div class="max-w-5xl mx-auto flex flex-col lg:flex-row px-4 py-4">
          <!-- Skeleton Content -->
          <!-- Image Placeholder -->
          <div class="bg-gray-200 h-64 lg:h-auto lg:w-60 rounded-2xl mb-4 lg:mb-0 lg:mr-4"></div>
          <!-- Card Container -->
          <div class="bg-white w-full p-6">
            <!-- Loading State Skeleton -->
            <div class="animate-pulse">
              <!-- Loading State Skeleton for Tags -->
              <div class="flex items-center space-x-4 mb-4">
                <div class="inline-block bg-gray-300 h-6 w-16 rounded-full"></div>
                <div class="inline-block bg-gray-300 h-6 w-16 rounded-full"></div>
                <div class="inline-block bg-gray-300 h-6 w-16 rounded-full"></div>
              </div>
              <!-- Loading State Skeleton for Title -->
              <div class="mb-4">
                <div class="h-8 w-3/4 bg-gray-300 rounded-full"></div>
              </div>
              <!-- Loading State Skeleton for Description -->
              <div class="mb-4">
                <div class="h-6 w-full bg-gray-300 rounded-full"></div>
                <div class="h-6 w-5/6 bg-gray-300 rounded-full"></div>
                <div class="h-6 w-3/4 bg-gray-300 rounded-full"></div>
              </div>
              <!-- Loading State Skeleton for Read more and Author section -->
              <div class="flex items-center justify-between mt-4">
                <div class="h-6 w-1/4 bg-gray-300 rounded-full"></div>
                <div class="flex items-center">
                  <div class="h-6 w-20 bg-gray-300 rounded-full"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
      <template v-else>
        <!-- Content Template -->
        <div class="max-w-5xl mx-auto flex flex-col lg:flex-row px-4 py-4">
          <!-- Actual Content -->
          <!-- Image -->
          <img src="https://helium.privateproperty.co.za/live-za-images/property/275/38/10176275/images/property-10176275-64564482_e.jpg" alt="Author Photo" class="object-cover h-64 lg:h-auto lg:w-60 rounded-2xl mb-4 lg:mb-0 lg:mr-4">
          <!-- Card Container -->
          <div class="bg-white w-full ">
            <div class="p-6">
              <div class="flex items-center space-x-4 mb-4">
                <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Mafikeng</span>
                <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Accredited</span>
                <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Tag #3</span>
              </div>
              <!-- Title -->
              <div class="mb-4 text-left "> <!-- Added text-left class -->
                <h2 class="text-2xl font-bold text-black hover:text-gray-600 dark:hover:text-gray-200 hover:underline cursor-pointer">SedibengVille</h2>
              </div>
              <!-- Description -->
              <div class="mb-4 text-left "> <!-- Added text-left class -->
                <h1 class="mt-2 font-bold text-black"> Univeristy Drive, Unit 5, Mafikeng</h1>
              </div>
              <!-- Description -->
              <div class="mb-4 text-left pb-6"> <!-- Added text-left class -->
                <p class="mt-2 font-bold text-black"> Nearest campus: Mafikeng</p>
              </div>
              <div class="w-1/4 md:w-full border-t border-gray-300"></div>
              <!-- Read more and Author section -->
              <div class="flex items-center justify-between mt-4">
                
                <router-link :to="{ name: 'details' }" class="px-4 py-4 transition duration-300 ease-in-out text-blue-600 dark:text-blue-400 hover:underline" :class="{ 'border-b-2 border-blue-500': $route.name === 'details', 'text-gray-500 border-indigo-400': isScrolled }">Details ⟶</router-link>
                <div class="flex items-center">
                  <a class="font-bold text-black cursor-pointer">John Doe</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SkeletonContent',
    data() {
      return {
        showSkeleton: true // Initially show the skeleton
      };
    },
    mounted() {
      // After 5 seconds, hide the skeleton
      setTimeout(() => {
        this.showSkeleton = false;
      }, 3000);
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styling here */
  .container {
    margin-top: 5rem;
  }
  </style>
  