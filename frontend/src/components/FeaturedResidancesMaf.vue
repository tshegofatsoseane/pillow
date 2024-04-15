<template>
  <div class="content-wrapper bg-white">
    <div class="text-gray-500 py-14 mb-1 mx-auto" style="max-width: 1450px;">
      <div class="text-center">
        <h1 class="text-4xl lg:text-4xl font-semibold mb-6 mx-4 md:mx-auto">Featured accommodations in Mafikeng</h1>
        <p hidden class="text-lg lg:text-xl mb-8 mx-auto">Discover comfortable and secure student accommodations near all NWU Campuses.</p>

        <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4 gap-8">
          <!-- Skeleton card for each accommodation -->
          <div v-for="index in 4" :key="index" class="bg-white w-full md:w-80 max-w-full mx-auto md:max-w-2xl md:mx-auto rounded-xl overflow-hidden animate-pulse">
            <div class="w-full h-80 bg-gray-200 rounded-xl"></div>
            <div class="px-1 py-4">
              <div class="h-8 bg-gray-200 mb-2 rounded-md"></div>
              <div class="h-4 bg-gray-200 rounded-md"></div>
            </div>
          </div> 
        </div>

        <div v-else-if="accommodations.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4 gap-8">
          <!-- Card for each accommodation -->
          <div v-for="accommodation in accommodations" :key="accommodation.id" class="bg-white w-full md:w-80 max-w-full mx-auto md:max-w-2xl md:mx-auto rounded-xl overflow-hidden">
            <img class="w-full h-80 object-cover rounded-xl" :src="accommodation.image_url" alt="Accommodation Image">
            <div class="px-1 py-4">
              <h2 class="text-xl font-semibold mb-2 text-left text-black">{{ accommodation.residence_name  }}</h2>
              <p class="text-gray-700 text-left mb-1">{{ accommodation.street_address }}</p>
            </div>
          </div> 
        </div>
        
        <!-- Display message if no accommodations are available -->
        <div v-else class="text-center text-gray-700">No accommodations available</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      accommodations: [],
      loading: true
    };
  },
  mounted() {
    this.fetchAccommodations();
  },
  methods: {
    async fetchAccommodations() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/accommodations/?q=mafikeng");
        const data = await response.json();
        this.accommodations = data.results.slice(0, 4);
        console.log(this.accommodations);
        this.loading = false;
      } catch (error) {
        console.error("Error fetching accommodations:", error);
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.content-wrapper {
  padding-top: 10px;
  padding-bottom: 80px;
}

@media (min-width: 768px) {
  .content-wrapper {
    padding-top: 10px;
    padding-bottom: 100px;
  }
}
</style>
