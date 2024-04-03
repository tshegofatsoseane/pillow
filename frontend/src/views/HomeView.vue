<template>
  <div class="home">
    <HomeNavBar />
    <Hero />

    <div>
      <!-- Correctly use SearchBox component -->
      <SearchBox @search-results-updated="updateSearchResults" />
      <!-- Move the "Showing results for" heading here -->
      <h1 v-if="searchResultsFromSearchBox.length" class="font-semibold">Showing results for "{{ searchResultsFromSearchBox[0]?.searchQuery }}"</h1>
      <!-- Display SearchResults component only if there are search results -->
      <SearchResults v-if="searchResultsFromSearchBox.length" :searchResults="searchResultsFromSearchBox" />
    </div>

    <FeaturedResidancesMaf />
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
import SearchBox from '@/components/SearchBox.vue' // Correct import statement
import HomeNavBar from '@/components/HomeNavBar.vue'

export default {
  name: 'HomeView',
  components: {
    HomeNavBar, Hero, FeaturedResidancesMaf, SearchBox, FeaturedResidancesPotch, FeaturedResidancesVaal, SearchResults
  },
  data() {
    return {
      searchResultsFromSearchBox: [] // Initialize an empty array to store search results passed from SearchBox component
    }
  },
  methods: {
    updateSearchResults(searchResults) {
  this.searchResultsFromSearchBox = searchResults;
  console.log('Search results updated:', this.searchResultsFromSearchBox);
}
  }
}
</script>
