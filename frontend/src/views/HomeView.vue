<template>
  <div class="home">
    <HomeNavBar />
    <Hero />

    <div>
     
      <SearchBox @search-results-updated="updateSearchResults" @search-loading="handleSearchLoading" />

      <h1 v-if="searchResultsFromSearchBox.length" class="font-semibold">Showing results for "{{ searchResultsFromSearchBox[0]?.searchQuery }}"</h1>
      <!-- Display SearchResults component only if there are search results -->
      <SearchResults v-if="searchResultsFromSearchBox.length" :searchResults="searchResultsFromSearchBox" />
    </div>

    <!-- Tabs for accommodations -->
    <div class="tabs mt-8">
      <ul class="rounded-md bg-gradient-to-r from-indigo-200 to-indigo-500 inline-flex justify-center space-x-8 px-4 py-2">
        <li v-for="tab in tabs" :key="tab.id" :class="{ 'active-tab': activeTab === tab.id }" @click="activeTab = tab.id" class="tab">
          <a href="#" class="tab-link">{{ tab.label }}</a>
        </li>
      </ul>
         <!-- Decorative line separator -->
           <div class="separator my-8"></div>

      <div v-if="activeTab === 'all'" class="tab-content">
        <NWUResidances />
        <UJResidances />
      </div>
      <div v-if="activeTab === 'nwu'" class="tab-content">
        <!-- Display NWU related accommodations -->
        <FeaturedResidancesMaf :accommodations="fetchedAccommodations.results.filter(accommodation => accommodation.university === 'NWU')" />
        <FeaturedResidancesPotch />
        <FeaturedResidancesVaal /> 
      </div>
      <div v-if="activeTab === 'uj'" class="tab-content">
        <!-- Display UJ related accommodations -->
        <UJResidances :accommodations="fetchedAccommodations.results.filter(accommodation => accommodation.university === 'UJ')" />
      </div>
      <div v-if="activeTab === 'ufs'" class="tab-content">
        <!-- Display UFS related accommodations -->
      </div>
      <div v-if="activeTab === 'wits'" class="tab-content">
        <!-- Display WITS related accommodations -->
      </div>
      
    </div>



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
import UJResidances from '@/components/UJResidances.vue'
import NWUResidances from '@/components/NWUResidances.vue'
import AllResidances from '@/components/AllResidances.vue'
import SearchResults from '@/components/SearchResults.vue'
import SearchBox from '@/components/SearchBox.vue'
import HomeNavBar from '@/components/HomeNavBar.vue'
import DetailBox from '@/components/DetailBox.vue'
import TestTabs from '@/components/TestTabs.vue'

export default {
  name: 'HomeView',
  components: {
   AllResidances, NWUResidances, UJResidances, TestTabs, DetailBox, HomeNavBar, Hero, FeaturedResidancesMaf, SearchBox, FeaturedResidancesPotch, FeaturedResidancesVaal, SearchResults
  },
  data() {
    return {
      searchResultsFromSearchBox: [],
      fetchedAccommodations: { results: [] },
      loading: false,
      activeTab: 'all',
      tabs: [
        { id: 'all', label: 'All' },
        { id: 'nwu', label: 'NWU' },
        { id: 'uj', label: 'UJ' },
        { id: 'ufs', label: 'UFS' },
        { id: 'wits', label: 'WITS' }
      ]
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
  height: 100%;
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
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}


.separator {
  height: 2px;
  background: linear-gradient(to right, #6a11cb, #2575fc);
  border-radius: 20px;
  width: 1300px;
  margin-left: 150px;
}


/* Custom styles for the tabs */
.tabs ul {
  border-radius: 30px;
}

.tab {
  @apply transition duration-300 ease-in-out cursor-pointer relative;
}

.tab-link {
  @apply block rounded-full px-6 py-3 text-lg font-medium leading-tight text-white focus:outline-none relative z-10 overflow-hidden;
  transition: transform 0.3s ease;
}

.tab-link:hover {
  transform: translateY(-3px);
}

.active-tab .tab-link {
  background: linear-gradient(120deg, #6a11cb 0%, #2575fc 100%);
}

@media screen and (max-width: 640px) {
  .tab-link {
    @apply px-4 py-2 text-base;
  }
}
</style>
