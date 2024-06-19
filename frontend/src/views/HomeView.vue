<template>
  <div class="home">
    <newbar />
    <Hero />

    <div>
     
      <SearchBox @search-results-updated="updateSearchResults" @search-loading="handleSearchLoading" />

      <h1 v-if="searchResultsFromSearchBox.length" class="font-semibold">Showing results for "{{ searchResultsFromSearchBox[0]?.searchQuery }}"</h1>
      <!-- Display SearchResults component only if there are search results -->
      <SearchResults v-if="searchResultsFromSearchBox.length" :searchResults="searchResultsFromSearchBox" />
    </div>

    <!-- Tabs for accommodations -->
    <div class="tabs mt-8">
      <ul class="tab-list">
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



    <!-- Display loader and overlay based on loading state 
    <div v-if="loading" class="loading-overlay">
      <div class="loader"></div>
    </div> -->
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
import newbar from '@/components/newbar.vue'

export default {
  name: 'HomeView',
  components: {
   AllResidances, newbar, NWUResidances, UJResidances, TestTabs, DetailBox, HomeNavBar, Hero, FeaturedResidancesMaf, SearchBox, FeaturedResidancesPotch, FeaturedResidancesVaal, SearchResults
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


.separator {
  height: 2px;
  background: whitesmoke;
  border-radius: 20px;
  width: 1300px;
  margin-left: 150px;
}


/* Custom styles for the tabs */
.tab-list {
  display: flex;
  gap: 16px;
  padding: 10px;
  background-color: #f3f4f6;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 600px;
  margin: 0 auto;
}


.tab {
  list-style: none;
  cursor: pointer;
  transition: transform 0.3s ease, background-color 0.3s ease;
}

.tab-link {
  display: block;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 500;
  color: #374151;
  text-decoration: none;
  transition: color 0.3s ease, background-color 0.3s ease;
}

.tab:hover {
  transform: translateY(-3px);
}

.tab-link:hover {
  background-color: #e5e7eb;
  color: #1f2937;
}

.active-tab .tab-link {
  background-color: #6366f1;
  color: #ffffff;
}

@media screen and (max-width: 640px) {
  .tab-link {
    padding: 8px 16px;
    font-size: 14px;
  }
}
</style>
