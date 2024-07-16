<template>
  <div class="home">
    <newbar />
    <Hero />

    <div>
      <SearchBox @search-results-updated="updateSearchResults" @search-loading="handleSearchLoading" />

      <h1 v-if="searchResultsFromSearchBox.length" class="font-semibold">
        Showing results for "{{ searchResultsFromSearchBox[0]?.searchQuery }}"
      </h1>
      <!-- Display SearchResults component only if there are search results -->
      <SearchResults v-if="searchResultsFromSearchBox.length" :searchResults="searchResultsFromSearchBox" />
    </div>

    <!-- Tabs for accommodations -->
    <AccommodationTabs :fetchedAccommodations="fetchedAccommodations" />

    <!-- Display loader and overlay based on loading state 
    <div v-if="loading" class="loading-overlay">
      <div class="loader"></div>
    </div> -->
    <Footer />
  </div>
</template>

<script>
import Hero from '@/components/Hero.vue'
import SearchResults from '@/components/SearchResults.vue'
import SearchBox from '@/components/SearchBox.vue'
import newbar from '@/components/newbar.vue'
import AccommodationTabs from '@/components/AccommodationTabs.vue'
import Footer from '@/components/Footer.vue'


export default {
  name: 'HomeView',
  components: {
    newbar,
    Hero,
    SearchBox,
    SearchResults,
    AccommodationTabs,
    Footer, 
  },
  data() {
    return {
      searchResultsFromSearchBox: [],
      fetchedAccommodations: { results: [] },
      loading: false,
    };
  },
  mounted() {
    this.fetchAccommodations();
  },
  methods: {
    async fetchAccommodations() {
      try {
        this.loading = true;
        const response = await fetch("http://127.0.0.1:8000/api/accommodations/");
        const data = await response.json();
        this.fetchedAccommodations = data;
      } catch (error) {
        console.error("Error fetching accommodations:", error);
      } finally {
        this.loading = false;
      }
    },
    async updateSearchResults(searchResults) {
      if (searchResults && searchResults.results) {
        const resultsArray = searchResults.results;
        resultsArray.forEach(result => {
          result.searchQuery = this.searchQuery;
        });
        this.searchResultsFromSearchBox = resultsArray;
      } else {
        console.error('Results array not found in searchResults:', searchResults);
      }
    },
    handleSearchLoading(loading) {
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
  height: 200%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
}

.loader {
  border: 10px solid #f3f3f3;
  border-top: 10px solid indigo;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
  margin-top: -1000px ;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
