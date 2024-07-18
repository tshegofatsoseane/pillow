<template>
  <div style="margin-top: -100px;" class="content-wrapper">
    <div class="container mx-auto max-w-screen-xl">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-2xl font-semibold text-gray-500">
          Featured Accommodations near {{ university }} - {{ campus }}
        </h1>
        <div>
          <button
            v-if="!showAll"
            @click="showAll = true"
            class="bg-indigo-500 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition duration-300"
          >
            Show All
          </button>
          <button
            v-else
            @click="showAll = false"
            class="bg-indigo-600 text-white px-4 py-2 rounded-full hover:bg-indigo-700 transition duration-300"
          >
            Show Less
          </button>
        </div>
      </div>

      <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <!-- Skeleton card for each accommodation -->
        <div v-for="index in 4" :key="index" class="relative animate-pulse">
          <div class="bg-white rounded-7xl cursor-pointer rounded-b-3xl overflow-hidden shadow-lg transition duration-300 transform hover:shadow-xl">
            <div class="h-60 w-full bg-gray-400 rounded-t-3xl"></div>
            <h2 class="absolute top-2 left-2 bg-white shadow-md bg-opacity-40 text-black rounded-md w-28 h-6 flex items-center justify-center">
              Accredited
            </h2>
            <button class="absolute top-2 right-2 bg-white shadow-md bg-opacity-40 text-black rounded-full w-10 h-10 flex items-center justify-center">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4c2.76 0 5 2.24 5 5 0 3.48-3.5 6.32-5 9.32-1.5-3-5-5.84-5-9.32 0-2.76 2.24-5 5-5z"></path>
              </svg>
            </button>
            <div class="px-4 py-4 flex flex-col justify-between">
              <div>
                <div class="h-6 bg-gray-400 rounded-md mb-2"></div>
                <div class="h-4 bg-gray-400 rounded-md"></div>
              </div>
              <div class="flex items-center mb-">
                <span class="text-lg font-semibold text-black mr-2">★★★★★ <span class="text-lg font-light text-gray-400">Rate this residence</span></span>
              </div>
              <div class="bottom-4 py-2 my-2 left-2 w-28 h-10 flex items-center justify-center bg-white border border-black text-black rounded-full hover:bg-gray-700 transition duration-300"></div>
            </div>
          </div>
        </div>
      </div>

      <div v-else>
        <div v-if="showAll">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div v-for="(accommodation) in accommodations" :key="accommodation.id" class="relative">
              <div class="bg-white rounded-7xl cursor-pointer rounded-b-3xl overflow-hidden shadow-lg transition duration-300 transform hover:shadow-xl">
                <img class="w-full h-60 object-cover rounded-t-3xl" :src="accommodation.image_url" alt="Accommodation Image" />
                <h2 class="absolute top-2 left-2 bg-white shadow-md bg-opacity-40 text-black rounded-md w-28 h-6 flex items-center justify-center">
                  Accredited
                </h2>
                <button class="absolute top-2 right-2 bg-white shadow-md bg-opacity-40 text-black rounded-full w-10 h-10 flex items-center justify-center">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4c2.76 0 5 2.24 5 5 0 3.48-3.5 6.32-5 9.32-1.5-3-5-5.84-5-9.32 0-2.76 2.24-5 5-5z"></path>
                  </svg>
                </button>
                <div class="px-4 py-4 h-60 flex flex-col justify-between">
                  <div>
                    <h2 class="text-xl text-left font-semibold text-gray-800 mb-2 overflow-hidden overflow-ellipsis whitespace-nowrap">
                      {{ accommodation.residence_name }}
                    </h2>
                    <p class="text-gray-600 text-left overflow-hidden overflow-ellipsis whitespace-nowrap">
                      {{ accommodation.street_address }}
                    </p>
                  </div>
                  <div class="flex items-center mb-">
                    <span class="text-lg font-semibold text-black mr-2">★★★★★ <span class="text-lg font-light text-gray-400">Rate this residence</span></span>
                  </div>
                  <router-link :to="{ name: 'details', params: { id: accommodation.id }, query: { residence_name: accommodation.residence_name, image_url: accommodation.image_url, street_address: accommodation.street_address, nearest_campus: accommodation.nearest_campus, cell_number: accommodation.cell_number, email: accommodation.email, map_url: accommodation.map_url, directions_url: accommodation.directions_url, streetview_url: accommodation.streetview_url  } }" class="bottom-4 py-2 my-2 left-2 w-28 h-10 flex items-center justify-center bg-white border border-black text-black rounded-full hover:bg-gray-700 transition duration-300">View details</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-else>
          <div
            ref="scrollContainer"
            class="scroll-container overflow-x-auto whitespace-nowrap"
            @mousedown="handleMouseDown"
            @mouseleave="handleMouseLeave"
            @mouseup="handleMouseUp"
            @mousemove="handleMouseMove"
          >
            <div v-for="(accommodation) in limitedAccommodations" :key="accommodation.id" class="inline-block relative mr-4 w-80">
              <div class="bg-white rounded-7xl cursor-pointer rounded-b-3xl overflow-hidden shadow-lg transition duration-300 transform hover:shadow-xl">
                <img class="w-full h-60 object-cover rounded-t-3xl" :src="accommodation.image_url" alt="Accommodation Image" />
                <h2 class="absolute top-2 left-2 bg-white shadow-md bg-opacity-40 text-black rounded-md w-28 h-6 flex items-center justify-center">
                  Accredited
                </h2>
                <button class="absolute top-2 right-2 bg-white shadow-md bg-opacity-40 text-black rounded-full w-10 h-10 flex items-center justify-center">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4c2.76 0 5 2.24 5 5 0 3.48-3.5 6.32-5 9.32-1.5-3-5-5.84-5-9.32 0-2.76 2.24-5 5-5z"></path>
                  </svg>
                </button>
                <div class="px-4 py-4 h-60 flex flex-col justify-between">
                  <div>
                    <h2 class="text-xl text-left font-semibold text-gray-800 mb-2 overflow-hidden overflow-ellipsis whitespace-nowrap">
                      {{ accommodation.residence_name }}
                    </h2>
                    <p class="text-gray-600 text-left overflow-hidden overflow-ellipsis whitespace-nowrap">
                      {{ accommodation.street_address }}
                    </p>
                  </div>
                  <div class="flex items-center mb-">
                    <span class="text-lg font-semibold text-black mr-2">★★★★★ <span class="text-lg font-light text-gray-400">Rate this residence</span></span>
                  </div>
                  <router-link :to="{ name: 'details', params: { id: accommodation.id }, query: { residence_name: accommodation.residence_name, image_url: accommodation.image_url, street_address: accommodation.street_address, nearest_campus: accommodation.nearest_campus, cell_number: accommodation.cell_number, email: accommodation.email, map_url: accommodation.map_url, directions_url: accommodation.directions_url, streetview_url: accommodation.streetview_url } }"
                  class="bottom-4 py-2 my-2 left-2 w-28 h-10 flex items-center justify-center bg-white border border-black text-black rounded-full hover:bg-gray-700 transition duration-300">View details</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="separator my-8"></div>
  </div>
</template>

<script>
export default {
  props: {
    university: {
      type: String,
      required: true,
    },
    campus: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      accommodations: [],
      loading: true,
      showAll: false,
      isDragging: false,
      startX: 0,
      scrollLeft: 0,
    };
  },
  computed: {
    limitedAccommodations() {
      return this.accommodations.slice(0, 8);
    },
  },
  created() {
    this.loadDataFromStorage();
    if (!this.accommodations.length) {
      this.fetchAccommodations();
    }
  },
  watch: {
    accommodations(newAccommodations) {
      localStorage.setItem(
        `accommodations_${this.university}_${this.campus}`,
        JSON.stringify(newAccommodations)
      );
    },
  },
  methods: {
    async fetchAccommodations() {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/accommodations/?university=${this.university}&nearest_campus=${this.campus}`
      );
      const data = await response.json();
      this.accommodations = data.results;
      this.loading = false;
    } catch (error) {
      console.error("Error fetching accommodations:", error);
      this.loading = false;
    }
  },
  loadDataFromStorage() {
    const storedData = localStorage.getItem(
      `accommodations_${this.university}_${this.campus}`
    );
    if (storedData) {
      this.accommodations = JSON.parse(storedData);
      this.loading = false;
    }
  },
  // other methods...


watch: {
  campus(newCampus) {
    this.fetchAccommodations();
  },
  accommodations(newAccommodations) {
    localStorage.setItem(
      `accommodations_${this.university}_${this.campus}`,
      JSON.stringify(newAccommodations)
    );
  },
},
    loadDataFromStorage() {
      const storedData = localStorage.getItem(
        `accommodations_${this.university}_${this.campus}`
      );
      if (storedData) {
        this.accommodations = JSON.parse(storedData);
        this.loading = false;
      }
    },
    handleMouseDown(event) {
      this.isDragging = true;
      this.startX = event.pageX - this.$refs.scrollContainer.offsetLeft;
      this.scrollLeft = this.$refs.scrollContainer.scrollLeft;
    },
    handleMouseLeave() {
      this.isDragging = false;
    },
    handleMouseUp() {
      this.isDragging = false;
    },
    handleMouseMove(event) {
      if (!this.isDragging) return;
      event.preventDefault();
      const x = event.pageX - this.$refs.scrollContainer.offsetLeft;
      const walk = (x - this.startX) * 2;
      this.$refs.scrollContainer.scrollLeft = this.scrollLeft - walk;
    },
  },
};
</script>

<style scoped>
.content-wrapper {
  padding-top: 60px;
  padding-bottom: 60px;
}

@media (min-width: 768px) {
  .content-wrapper {
    padding-top: 100px;
    padding-bottom: 100px;
  }
}

.animate-pulse {
  animation: pulse 1.5s infinite ease-in-out;
}

@keyframes pulse {
  0%,
  100% {
    opacity: 0.4;
  }
  50% {
    opacity: 1;
  }
}

.separator {
  height: 2px;
  background: whitesmoke;
  border-radius: 50px;
}

.scroll-container {
  cursor: grab;
}

.scroll-container:active {
  cursor: grabbing;
}

.container {
  margin-top: -100px;
}
</style>

