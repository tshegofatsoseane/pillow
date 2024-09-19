<template>
  <div class="flex h-screen px-8 py-4">
    <!-- Left Sidebar: Search Results -->
    <div class="w-1/3 bg-gray-100 p-4 rounded-lg shadow-lg overflow-y-auto">
      <!-- Toolbar for Search Results -->
      <div class="mb-4 flex justify-between items-center">
        <h2 class="text-xl font-semibold text-gray-800">Search Results</h2>
        <button @click="clearSearch" class="text-blue-600 hover:text-blue-700 font-medium transition">
          Clear Search
        </button>
      </div>
      
      <!-- Search Bar -->
      <div class="mb-6">
        <input
          type="text"
          placeholder="Search accommodation"
          class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
          ref="searchInput"
        />
      </div>

      <!-- Loop through paginatedResults array and display each search result -->
      <div
        v-for="result in paginatedResults"
        :key="result.id"
        class="mb-6 p-6 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300"
        @click="selectResult(result)"
      >
        <!-- Image -->
        <div class="relative mb-4">
          <img
            :src="result.image_url"
            alt="Accommodation Image"
            class="object-cover w-full h-48 rounded-lg"
          />
          <span class="absolute top-4 left-4 bg-indigo-600 text-white text-xs px-2 py-1 rounded-md shadow-sm">
            {{ result.nearest_campus }}
          </span>
        </div>

        <!-- Content -->
        <div>
          <!-- Residence Name and Address -->
          <div class="mb-2">
            <h3 class="text-lg font-semibold text-gray-900 leading-tight">
              {{ result.residence_name }}
            </h3>
            <p class="text-sm text-gray-600">{{ result.street_address }}</p>
          </div>

          <!-- Tags -->
          <div class="flex flex-wrap gap-2 mb-4">
            <span
              v-for="tag in result.tags"
              :key="tag.id"
              class="px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 border border-gray-300 rounded-full"
            >
              {{ tag.name }}
            </span>
          </div>

          <!-- Details and Actions -->
          <div class="flex justify-between items-center">
            <router-link
              :to="{
                name: 'details',
                params: {
                  id: result.id,
                  residence_name: result.residence_name,
                  image_url: result.image_url,
                  street_address: result.street_address,
                  nearest_campus: result.nearest_campus
                }
              }"
              class="text-sm font-medium text-indigo-600 hover:text-indigo-700 transition"
            >
              View Details ⟶
            </router-link>
            <button class="px-4 py-2 text-sm text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg shadow-sm transition">
              Book Now
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Right Side: Map Section -->
    <div class="w-2/3 relative bg-gray-200 rounded-lg shadow-lg overflow-hidden">
      <!-- Amenities Toolbar on Top of the Map -->
      <div class="absolute top-0 left-0 right-0 p-4 bg-white shadow-md z-10 flex items-center justify-between space-x-4">
        <div class="flex items-center space-x-4">
          <h2 class="text-xl font-semibold text-gray-800">Map Amenities</h2>
          <select
            v-model="selectedCampus"
            @change="filterMapAmenities"
            class="p-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
          >
            <option value="">Select Campus</option>
            <option v-for="campus in uniqueCampuses" :key="campus.id" :value="campus.id">
              {{ campus.name }}
            </option>
          </select>
        </div>
        <button @click="filterMapAmenities" class="text-blue-600 hover:text-blue-700 font-medium transition">
          Filter
        </button>
      </div>
      
      <!-- Map iframe -->
      <div v-if="selectedMapUrl" class="absolute inset-0 top-16">
        <iframe
          :src="selectedMapUrl"
          width="100%"
          height="100%"
          style="border:0;"
          allowfullscreen=""
          loading="lazy"
        ></iframe>
      </div>
      
      <!-- Placeholder for Map -->
      <div v-else class="absolute inset-0 top-16 flex items-center justify-center">
        <span class="text-gray-500 font-medium text-xl">Select a search result to view map</span>
      </div>

      <!-- Colleagues Info (Bottom Right) -->
      <div class="absolute bottom-6 right-6 bg-white p-4 rounded-lg shadow-lg">
        <p class="text-sm font-semibold text-gray-800">My Colleagues</p>
        <p class="text-xs text-gray-500">{{ colleagues.total }} Total, {{ colleagues.nearby }} Nearby, {{ colleagues.online }} Online</p>
        <div class="flex space-x-2 mt-2">
          <img
            v-for="colleague in colleagues.list"
            :key="colleague.id"
            :src="colleague.image_url"
            class="w-8 h-8 rounded-full border-2 border-white shadow-sm"
            alt="Colleague Avatar"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchResults",
  props: {
    searchResults: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      currentPage: 1,
      pageSize: 10,
      campuses: [], // Will be populated based on search results
      selectedCampus: '', // Stores the selected campus
      colleagues: {
        total: 25,
        nearby: 10,
        online: 8,
        list: [
          { id: 1, image_url: "https://randomuser.me/api/portraits/men/1.jpg" },
          { id: 2, image_url: "https://randomuser.me/api/portraits/women/2.jpg" },
          // Add more colleague images here
        ],
      },
      selectedMapUrl: null, // Stores the selected map URL
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
    },
    uniqueCampuses() {
      const campuses = this.searchResults.flatMap(result => result.nearest_campus);
      const uniqueCampuses = Array.from(new Set(campuses.map(campus => campus.id)))
        .map(id => campuses.find(campus => campus.id === id));
      return uniqueCampuses;
    },
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
    },
    selectResult(result) {
      this.selectedMapUrl = result.map_url;
      this.selectedCampus = ''; // Reset selected campus when changing results
    },
    clearSearch() {
      this.$refs.searchInput.value = '';
    },
    clearMap() {
      this.selectedMapUrl = null;
      this.selectedCampus = '';
    },
    filterMapAmenities() {
      console.log('Filtering map amenities for campus:', this.selectedCampus);
    },
  },
  mounted() {
    if (this.searchResults.length > 0) {
      this.selectedMapUrl = this.searchResults[0].map_url;
    }
  },
};
</script>

<style scoped>
/* Custom styles for a clean, professional design */
body {
  font-family: 'Inter', sans-serif;
}

.bg-gray-100 {
  background-color: #f3f4f6;
}

.bg-gray-200 {
  background-color: #e5e7eb;
}

.bg-indigo-600 {
  background-color: #5a67d8;
}

.text-gray-800 {
  color: #1f2937;
}

.text-gray-600 {
  color: #718096;
}

/* Hover effects */
button:hover {
  transform: translateY(-2px);
  transition: all 0.2s ease-in-out;
}

a:hover {
  text-decoration: underline;
}

/* Map container style */
iframe {
  border: 0;
}
</style>
