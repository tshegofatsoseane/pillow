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
        />
      </div>

      <!-- Loop through paginatedResults array and display each search result -->
      <div
        v-for="result in paginatedResults"
        :key="result.id"
        class="mb-6 p-4 border rounded-lg bg-white hover:shadow-md transition-shadow duration-300"
        @click="selectResult(result)"
      >
        <!-- Image -->
        <img
          :src="result.image_url"
          alt="Accommodation Image"
          class="object-cover w-full h-48 rounded-lg mb-4 shadow-md"
        />

        <!-- Content -->
        <div>
          <!-- Residence Name and Address -->
          <div class="mb-2 text-left">
            <span class="text-lg font-semibold text-gray-800">{{ result.residence_name }}</span>
            <div class="text-sm text-gray-600">{{ result.street_address }}</div>
          </div>

          <!-- Tags (e.g., Free EV, Lockers, Pets Allowed, Vegan) -->
          <div class="flex flex-wrap space-x-2 mb-4">
            <span
              v-for="tag in result.tags"
              :key="tag.id"
              class="px-3 py-1 text-xs font-semibold text-white bg-indigo-500 rounded-full shadow-sm"
            >
              {{ tag.name }}
            </span>
          </div>

          <!-- Details and Booking Button -->
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
              class="text-blue-600 hover:text-blue-700 font-medium transition"
            >
              View Details ⟶
            </router-link>
            <button class="px-4 py-2 text-white bg-blue-500 rounded-lg hover:bg-blue-600 transition">
              Book Now
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Right Side: Map Section -->
    <div class="w-2/3 relative bg-gray-200 rounded-lg shadow-lg overflow-hidden">
      <!-- Toolbar for Map Section -->
      <div class="absolute top-0 left-0 right-0 p-4 flex justify-between items-center bg-white shadow-md">
        <h2 class="text-xl font-semibold text-gray-800">Map</h2>
        <button @click="clearMap" class="text-blue-600 hover:text-blue-700 font-medium transition">
          Clear Map
        </button>
      </div>
      
      <!-- Map iframe -->
      <div v-if="selectedMapUrl" class="absolute inset-0">
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
      <div v-else class="absolute inset-0 flex items-center justify-center">
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
    },
    clearSearch() {
      // Clear search logic
      this.$refs.searchInput.value = '';
    },
    clearMap() {
      // Clear map logic
      this.selectedMapUrl = null;
    },
  },
  mounted() {
    // Set the initial map URL to the first result
    if (this.searchResults.length > 0) {
      this.selectedMapUrl = this.searchResults[0].map_url;
    }
  },
};
</script>

<style scoped>
/* Custom styles for a more modern design */
body {
  font-family: 'Inter', sans-serif;
}

.bg-gray-100 {
  background-color: #f3f4f6;
}

.bg-gray-200 {
  background-color: #e5e7eb;
}

.bg-blue-500 {
  background-color: #8265f7;
}

.bg-blue-600 {
  background-color: #8265f7;
}

.bg-green-500 {
  background-color: #10b981;
}

.bg-green-600 {
  background-color: #059669;
}

.text-gray-800 {
  color: #1f2937;
}

.text-gray-500 {
  color: #6b7280;
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
