<template>
  <div>
    <!-- Loop through searchResults array and display each search result -->
    <div v-for="result in searchResults" :key="result.id" class="max-w-5xl mx-auto flex flex-col lg:flex-row px-4 py-4">
      <!-- Actual Content -->
      <!-- Image -->
      <img :src="result.image_url" alt="Street View Image" class="object-cover h-64 lg:h-auto lg:w-60 rounded-2xl mb-4 lg:mb-0 lg:mr-4">
      <!-- Card Container -->
      
      <div class="bg-white w-full ">
        <div class="p-6">
          <div class="flex items-center space-x-4 mb-4">
            <!-- Display tags -->
            <span v-for="tag in result.tags" :key="tag.id" class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">{{ tag.name }}</span>
          </div>
          <!-- Title -->
          <div class="mb-4 text-left "> <!-- Added text-left class -->
            <h2 class="text-2xl font-bold text-black hover:text-gray-600 dark:hover:text-gray-200 hover:underline cursor-pointer">{{ result.residence_name }}</h2>
          </div>
          <!-- Description -->
          <div class="mb-4 text-left "> <!-- Added text-left class -->
            <h1 class="mt-2 font-bold text-black">{{ result.street_address }}</h1>
          </div>
          <!-- Nearest campus -->
          <div class="mb-4 text-left pb-6"> <!-- Added text-left class -->
            <p class="mt-2 font-bold text-black"> Nearest campus: {{ result.nearest_campus }}</p>
          </div>
          <!-- Read more and Author section -->
          <div class="flex items-center justify-between mt-4">
            <!-- Add your router-link or other navigation logic here -->
            <a class="font-bold text-black cursor-pointer">John Doe</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchResults',
  props: {
    searchResults: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<!-- Your existing style code -->
