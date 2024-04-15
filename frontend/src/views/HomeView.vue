<template>
  <div class="home">
    <HomeNavBar />
    <Hero />

    <div>
      <!-- Correctly use SearchBox component -->
      <SearchBox @search-results-updated="updateSearchResults" />
      <!-- Move the "Showing results for" heading inside the div -->
      <h1 v-if="searchResultsFromSearchBox.length" class="font-semibold">Showing results for "{{ searchResultsFromSearchBox[0]?.searchQuery }}"</h1>
      <!-- Display SearchResults component only if there are search results -->
      <SearchResults v-if="searchResultsFromSearchBox.length" :searchResults="searchResultsFromSearchBox" />
    </div>

    <!-- Pass only the results array as the accommodations prop -->
    <FeaturedResidancesMaf :accommodations="fetchedAccommodations.results" />
    <FeaturedResidancesPotch />
    <FeaturedResidancesVaal />
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
      searchResultsFromSearchBox: [], // Initialize an empty array to store search results passed from SearchBox component
      fetchedAccommodations: { results: [] } // Initialize with results array
    }
  },
  mounted() {
    // Fetch accommodations data when the component is mounted
    this.fetchAccommodations();
  },
  methods: {
    async fetchAccommodations() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/accommodations/?q=mafikeng");
        const data = await response.json();
        this.fetchedAccommodations = data;
        console.log(this.fetchAccommodations)
      } catch (error) {
        console.error("Error fetching accommodations:", error);
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
    }
  }
}
</script>
