<template>
  <div>
    <!-- Loop through searchResults array and display each search result -->
    <div v-for="result in paginatedResults" :key="result.id" class="max-w-5xl mx-auto flex flex-col lg:flex-row px-4 py-4">
      <!-- Actual Content -->
      <!-- Image -->
      <img :src="result.image_url" alt="Street View Image" class="object-cover h-64 lg:h-auto lg:w-60 rounded-2xl mb-4 lg:mb-0 lg:mr-4">
      <!-- Card Container -->
      <div class="bg-white w-full ">
        <div class="p-6">
          <!-- Content -->
          <div class="flex items-center space-x-4 mb-4">
            <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Mafikeng</span>
            <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Accredited</span>
            <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Tag #3</span>
          </div>
          <div class="flex items-center space-x-4 mb-4">
            <!-- Display tags -->
            <span v-for="tag in result.tags" :key="tag.id" class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">{{ tag.name }}</span>
          </div>
          <!-- Title -->
          <div class="mb-4 text-left ">
            <h2 class="text-2xl font-bold text-black hover:text-gray-600 dark:hover:text-gray-200 hover:underline cursor-pointer">{{ result.residence_name }}</h2>
          </div>
          <!-- Description -->
          <div class="mb-4 text-left ">
            <h1 class="mt-2 font-bold text-black">{{ result.street_address }}</h1>
          </div>
          <!-- Nearest campus -->
          <div class="mb-4 text-left pb-6">
            <p class="mt-2 font-bold text-black"> Nearest campus: {{ result.nearest_campus }}</p>
          </div>
          <div class="w-1/4 md:w-full border-t border-gray-300"></div>
          <!-- Read more and Author section -->
          <div class="flex items-center justify-between mt-4">
            <!-- Add your router-link or other navigation logic here -->
            <router-link :to="{ name: 'details', params: { id: result.id }, query: { residence_name: result.residence_name, image_url: result.image_url, street_address: result.street_address, nearest_campus: result.nearest_campus, cell_number: result.cell_number, email: result.email, map_url: result.map_url, directions_url: result.directions_url, streetview_url: result.streetview_url  } }" class="px-4 py-4 transition duration-300 ease-in-out text-blue-600 dark:text-blue-400 hover:underline">Details ⟶</router-link>

            <a class="font-bold text-black cursor-pointer">John Doe</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div class="flex justify-center mt-4">
      <button @click="previousPage" :disabled="currentPage === 1" class="pagination-button">Previous</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages" class="pagination-button">Next</button>
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
  },
  data() {
    return {
      currentPage: 1,
      pageSize: 10
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.searchResults.length / this.pageSize);
    },
    paginatedResults() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.searchResults.slice(startIndex, endIndex);
    }
  },
  methods: {
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    }
  }
};
</script>

<style scoped>
/* Pagination Button Styles */
.pagination-button {
  background-color: #4B5563;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  margin: 0 0.5rem;
}

.pagination-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
