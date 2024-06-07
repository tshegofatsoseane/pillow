<template>
  <div class="search-box-wrapper py-1" style="margin-top: -180px;">
    <div class="inset-0 bg-white bg-opacity-40 backdrop-blur-xl  rounded-xl shadow-md p-8 md:p-12 md:max-w-xl mx-auto mb-16 md:mt-20"  style="margin-top: -30px;">
      <h2 class="text-gray-700 lg:text-2xl mb-8 md:mb-12 mx-auto font-medium text-center">Search for residences</h2>
      


      <!-- Location Button -->
      <div class="flex items-center justify-center mb-4 md:mb-6"> 
        <button @click="submit" class="location-button p-3 md:p-4 rounded-xl bg-white border border-gray-300 hover:bg-white flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 md:h-10 md:w-10 text-indigo-500" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 2a5 5 0 00-5 5c0 3.866 5 10 5 10s5-6.134 5-10a5 5 0 00-5-5zm0 7a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>

      <!-- "Or" Text with Gray Lines -->
      <div class="flex items-center justify-center mb-4 md:mb-6">
        <div class="w-1/4 md:w-1/5 border-t border-gray-300"></div>
        <div class="mx-4 text-gray-400">or</div>
        <div class="w-1/4 md:w-1/5 border-t border-gray-300"></div>
      </div>

            <!-- University Filter Dropdown -->
            <div class="mb-4 md:mb-6">
        <select v-model="selectedUniversity" class="university-select p-3 md:p-4 rounded-xl bg-white border border-gray-300 w-full">
          <option disabled value="">Select a university</option>
          <option value="NWU">NWU</option>
          <option value="UFS">UFS</option>
          <option value="UJ">UJ</option>
          <option value="WITS">WITS</option>
        </select>
      </div>

      <!-- Search Input -->
      <div class="mb-4 md:mb-6">
        <input v-model="searchQuery" type="text" class="search-input p-3 md:p-4" placeholder="Enter your search...">
        <span class="search-icon"></span>
      </div>

      <!-- Loading Animation -->
      <div v-if="loading" class="loading-overlay">
        <div class="loader"></div>
      </div>

      <!-- Submit Button -->
      <button @click="submit" :disabled="loading" class="submit-button mt-10 p-6 md:p-4 w-full">
        {{ loading ? 'Loading...' : 'Submit Search' }}
      </button>
    </div>
    <h1 hidden class="font-semibold">Showing results for "{{ searchQuery }}"</h1>
  </div>
</template>

<script>
import axios from 'axios';
import SearchResults from './SearchResults.vue';

export default {
  name: 'SearchBox',
  components: {
    SearchResults
  },
  data() {
    return {
      loading: false,
      searchQuery: '',
      selectedUniversity: '', // Add a property to store the selected university
      searchResults: [] // Add a property to store search results
    };
  },
  methods: {
    async submit() {
      this.loading = true;
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/accommodations/', {
          params: {
            q: this.searchQuery,
            university: this.selectedUniversity // Include the selected university in the request parameters
          }
        });
        this.searchResults = response.data; // Assign response data to searchResults property
        // Emit only the search results array to the parent component
        this.$emit('search-results-updated', this.searchResults);
        window.scrollTo({
          top: 850,
          behavior: 'smooth'
       });
      } catch (error) {
        console.error('Error fetching search results:', error);
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.university-select {
  padding: 0.75rem 1rem;
  border: 1px solid #E5E7EB;
  border-radius: 0.5rem;
  width: 100%;
  transition: border-color 0.3s ease;
}

.university-select:focus {
  outline: none;
  border-color: #9CA3AF;
}

.search-input {
  padding: 0.75rem 1rem;
  border: 1px solid #E5E7EB;
  border-radius: 0.5rem;
  width: 100%;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #9CA3AF;
}

.search-icon {
  position: absolute;
  top: 50%;
  right: 1.5rem;
  transform: translateY(-50%);
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
}

.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.submit-button {
  background-color: #4B5563;
  color: white;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #2D3748;
}

.location-button {
  width: 80px;
  height: 60px;
}

.location-button:hover {
  border: 1px solid indigo;
}

/* Loader animation */
.loader {
  border-top-color: transparent !important;
  animation: spin 1s infinite linear;
}

.search-box-wrapper {
  width: calc(100% - 50px); /* Adjust as needed */
  margin-left: auto;
  margin-right: auto;
  margin-top: calc(100% - 50px);
}

@media (max-width: 640px) {
  .search-box-wrapper {
    margin-top: -100px; /* Adjust as needed */
  }
}
</style>
