<template>
  <div class="flex h-screen px-8 py-4 space-x-8" style="margin-top: 50px;">
    <!-- Left Sidebar: Search Results -->
    <div class="w-2/2 bg-gray-100 p-4 rounded-lg shadow-lg overflow-y-auto h-screen mt-6" >
  <!-- Sticky Toolbar and Search Bar Container -->
  <div class="sticky top-0 bg-gray-100 z-10 pt-2 pb-2"> 
  <!-- Toolbar for Search Results -->
  <div class="h-6 flex justify-between items-center mb-1">
    <h2 class="text-xl font-semibold text-gray-800">Search Results</h2>
    <button @click="clearSearch" class="text-blue-600 hover:text-blue-700 font-medium transition">
      Clear Search
    </button>
  </div>

  <!-- Search Bar -->
  <div hidden class="mb-6">
    <input
      type="text"
      placeholder="Search accommodation"
      class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
      ref="searchInput"
    />
  </div>
</div>

<!-- Loop through paginatedResults array and display each search result -->
<div class="grid grid-cols-1 lg:grid-cols-3 gap-6 " >
  <div
    v-for="result in paginatedResults"
    :key="result.id"
    class="p-0 bg-white border-2 border-gray-300 rounded-lg shadow-sm hover:shadow-lg hover:border-indigo-300 transition-shadow duration-300"
    @click="selectResult(result)"
  >
    <!-- Image -->
    <div class="relative mb-4">
      <img
        :src="result.image_url"
        alt="Accommodation Image"
        class="object-cover w-full rounded-t-lg h-48"
      />
      <span class="absolute top-4 left-4 bg-indigo-100 text-black text-xs px-2 py-1 rounded-md shadow-sm">
        {{ result.nearest_campus }}
      </span>
    </div>

    <!-- Content -->
    <div class="text-left p-1 ">
      <!-- Residence Name and Address -->
      <div class="mb-2">
        <h3 class="text-lg font-semibold text-gray-900 leading-tight overflow-hidden overflow-ellipsis whitespace-nowrap">
          {{ result.residence_name }}
        </h3>
        <p class="text-sm text-gray-600 overflow-hidden overflow-ellipsis whitespace-nowrap">{{ result.street_address }}</p>
      </div>

      <div class="flex items-center mb-">
                <span class="text-sm font-semibold text-black mr-2">★★★★★ <span class="text-md font-light text-gray-400 overflow-hidden overflow-ellipsis whitespace-nowrap">Rate this residence</span></span>
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
      <div class="flex justify-between items-center mt-2">
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
        
          class="text-sm font-medium bottom-4 py-2 my-2 left-2 w-28 h-8 flex items-center justify-center bg-white border border-black text-black rounded-full hover:bg-gray-700 transition duration-300"
        >
          View Details ⟶
        </router-link>
        <button class="bottom-4 py-2 my-2 left-2 w-28 h-10 items-center justify-center bg-white border border-black text-black rounded-full hover:bg-gray-700 transition duration-300 hidden">
          Book Now
        </button> 
      </div>
    </div>
  </div>
</div>
</div>


    <!-- Right Side: Map Section -->
    <section class="w-1/2 relative bg-white rounded-lg shadow-md mt-6">
      <!-- Toolbar with Map Filters -->
      <div class="absolute top-0 left-0 right-0 p-4 bg-gray-50 shadow-md flex justify-between items-center">
        <div class="flex items-center space-x-4">
          <h2 class="text-xl font-semibold text-gray-900">Map</h2>
          <select
            v-model="selectedCampus"
            @change="filterMapAmenities"
            class="p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">Select Campus</option>
            <option v-for="campus in uniqueCampuses" :key="campus.id" :value="campus.id">
              {{ campus.name }}
            </option>
          </select>
        </div>
        <button
          @click="filterMapAmenities"
          class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
        >
          Filter
        </button>
      </div>
      
      <!-- Map Display -->
      <div v-if="selectedMapUrl" class="absolute inset-0 top-16">
        <iframe
          :src="selectedMapUrl"
          class="w-full h-full"
          style="border: 0;"
          allowfullscreen=""
          loading="lazy"
        ></iframe>
      </div>
      
      <!-- Placeholder Text for Map -->
      <div v-else class="absolute inset-0 top-16 flex items-center justify-center">
        <p class="text-gray-500 text-lg">Select a search result to view map</p>
      </div>

      <!-- Colleagues Information Section -->
      <div class="absolute bottom-20 right-6 bg-white p-4 rounded-lg shadow-md">
        <h4 class="text-sm font-semibold text-gray-800">Colleagues</h4>
        <p class="text-xs text-gray-500">{{ colleagues.total }} Total, {{ colleagues.nearby }} Nearby</p>
        <div class="mt-2 flex space-x-2">
          <img
            v-for="colleague in colleagues.list"
            :key="colleague.id"
            :src="colleague.image_url"
            alt="Colleague Avatar"
            class="w-8 h-8 rounded-full border-2 border-white"
          />
        </div>
      </div>
    </section>
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
      campuses: [], 
      selectedCampus: '', 
      colleagues: {
        total: 25,
        nearby: 10,
        online: 8,
        list: [
          { id: 1, image_url: "https://randomuser.me/api/portraits/men/1.jpg" },
          { id: 2, image_url: "https://randomuser.me/api/portraits/women/2.jpg" },
        ],
      },
      selectedMapUrl: null,
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
    selectResult(result) {
      this.selectedMapUrl = result.map_url;
      this.selectedCampus = '';
    },
    clearSearch() {
      this.$refs.searchInput.value = '';
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
/* Custom Styles */
body {
  font-family: 'Inter', sans-serif;
}

.text-left {
 margin-left: 10px;
 margin-top: -10px;
}

.bg-gray-50 {
  background-color: #f9fafb;
}

.bg-white {
  background-color: white;
}

.text-gray-900 {
  color: #1a202c;
}

.text-gray-600 {
  color: #718096;
}

.text-blue-600 {
  color: #3182ce;
}

.text-blue-800 {
  color: #2b6cb0;
}

.border-gray-300 {
  border-color: #e2e8f0;
}

/* Button hover effects */
button:hover {
  transform: translateY(-1px);
  transition: all 0.2s ease-in-out;
}
</style>