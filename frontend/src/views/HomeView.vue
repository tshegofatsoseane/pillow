<template>
  <div class="home">
    <HomeNavBar />
    <Hero />

    <div>
      <!-- Correctly use SearchBox component -->
      <SearchBox @search-results-updated="updateSearchResults" @search-loading="handleSearchLoading" />
      <!-- Move the "Showing results for" heading inside the div -->
      <h1 v-if="searchResultsFromSearchBox.length" class="font-semibold">Showing results for "{{ searchResultsFromSearchBox[0]?.searchQuery }}"</h1>
      <!-- Display SearchResults component only if there are search results -->
      <SearchResults v-if="searchResultsFromSearchBox.length" :searchResults="searchResultsFromSearchBox" />
    </div>

    <!-- Pass only the results array as the accommodations prop -->
    <FeaturedResidancesMaf :accommodations="fetchedAccommodations.results" />
    <FeaturedResidancesPotch />
    <FeaturedResidancesVaal />

    <!-- Display loader and overlay based on loading state -->
    <div v-if="loading" class="loading-overlay">
      <div class="loader"></div>
    </div>
  </div>
</template>

<script>
import Hero from '@/components/Hero.vue'
import FeaturedResidancesMaf from '@/components/FeaturedResidancesMaf.vue'
import FeaturedResidancesPotch from '@/components/FeaturedResidancesPotch.vue'
import FeaturedResidancesVaal from '@/components/FeaturedResidancesVaal.vue'
import SearchResults from '@/components/SearchResults.vue'
import SearchBox from '@/components/SearchBox.vue'
import HomeNavBar from '@/components/HomeNavBar.vue'
import DetailBox from '@/components/DetailBox.vue'

export default {
  name: 'HomeView',
  components: {
    DetailBox, HomeNavBar, Hero, FeaturedResidancesMaf, SearchBox, FeaturedResidancesPotch, FeaturedResidancesVaal, SearchResults
  },
  data() {
    return {
      searchResultsFromSearchBox: [],
      fetchedAccommodations: { results: [] },
      loading: false // Ensure that loading is initially set to false
    };
  },
  mounted() {
    // Fetch accommodations data when the component is mounted
    this.fetchAccommodations();
  },
  methods: {
    async fetchAccommodations() {
      try {
        this.loading = true; // Set loading to true before fetching data
        const response = await fetch("http://127.0.0.1:8000/api/accommodations/?q=mafikeng");
        const data = await response.json();
        this.fetchedAccommodations = data;
        console.log(this.fetchAccommodations);
      } catch (error) {
        console.error("Error fetching accommodations:", error);
      } finally {
        this.loading = false; // Set loading to false after fetching data
      }
    },
    async updateSearchResults(searchResults) {
      if (searchResults && searchResults.results) {
        const resultsArray = searchResults.results;
        // Add searchQuery property to each result object
        resultsArray.forEach(result => {
          result.searchQuery = this.searchQuery;
        });
        this.searchResultsFromSearchBox = resultsArray;
        console.log('Search results updated:', this.searchResultsFromSearchBox);
      } else {
        console.error('Results array not found in searchResults:', searchResults);
      }
    },
    handleSearchLoading(loading) {
      // Update loading state based on the event emitted from SearchBox component
      this.loading = loading;
    }
  }
}
</script>

<style scoped>
/* Add your styles for loading overlay and loader here */
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
</style>
