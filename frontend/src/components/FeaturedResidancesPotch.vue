<template>
<div class="content-wrapper">
  <div class="container mx-auto max-w-screen-xl">
    <h1 class="text-4xl font-semibold text-center text-gray-800 mb-8">Featured Accommodations in Potchefstroom</h1>

    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      <!-- Skeleton card for each accommodation -->
      <div v-for="index in 4" :key="index" class="animate-pulse">
        <div class="bg-gray-200 rounded-xl overflow-hidden">
          <div class="h-80 w-full bg-gray-400 rounded-t-xl"></div>
          <div class="px-4 py-4">
            <div class="h-6 bg-gray-400 rounded-md mb-2"></div>
            <div class="h-4 bg-gray-400 rounded-md"></div>
          </div>
        </div>
      </div> 
    </div>

    <div v-else-if="accommodations.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      <!-- Card for each accommodation -->
      <div v-for="accommodation in accommodations" :key="accommodation.id" class="relative">
        <div class="bg-white rounded-7xl cursor-pointer rounded-b-3xl overflow-hidden shadow-lg transition duration-300 transform hover:shadow-xl">
          <img class="w-full h-60 object-cover rounded-t-3xl" :src="accommodation.image_url" alt="Accommodation Image">

          <h2 class="absolute top-2 left-2 bg-white shadow-md bg-opacity-40 text-black rounded-md w-28 h-6 flex items-center justify-center">
            Accredited
          </h2>


          <button class="absolute top-2 right-2 bg-white shadow-md bg-opacity-40  text-black rounded-full w-10 h-10 flex items-center justify-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4c2.76 0 5 2.24 5 5 0 3.48-3.5 6.32-5 9.32-1.5-3-5-5.84-5-9.32 0-2.76 2.24-5 5-5z"></path>
            </svg>
          </button>
          <div class="px-4 py-4 h-60 flex flex-col justify-between"> <!-- Fixed height for card body -->
            <div>
              <h2 class="text-xl text-left font-semibold text-gray-800 mb-2 overflow-hidden overflow-ellipsis whitespace-nowrap">{{ accommodation.residence_name }}</h2>
              <p class="text-gray-600 text-left overflow-hidden overflow-ellipsis whitespace-nowrap">{{ accommodation.street_address }}</p>
            </div>
            <div class="flex items-center mb-">
              <span class="text-lg font-semibold text-black mr-2">★★★★★ <span  class="text-lg font-light text-gray-400" >Rate this residance</span> </span>
            </div>

            <router-link :to="{ name: 'details', params: { id: accommodation.id }, query: { residence_name: accommodation.residence_name, image_url: accommodation.image_url, street_address: accommodation.street_address, nearest_campus: accommodation.nearest_campus, cell_number: accommodation.cell_number, email: accommodation.email, map_url: accommodation.map_url, directions_url: accommodation.directions_url, streetview_url: accommodation.streetview_url  } }" class="bottom-4 py-2 my-2 left-2 w-28 h-10 flex items-center justify-center  bg-white border border-black text-black rounded-full hover:bg-gray-700 transition duration-300">View details</router-link>
          </div>
        </div> 
      </div>
    </div>
    
    <!-- Display message if no accommodations are available -->
    <div v-else class="text-center text-gray-700 mt-8">No accommodations available</div>
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
      const response = await fetch("http://127.0.0.1:8000/api/accommodations/?q=potchefstroom");
      const data = await response.json();
      
      // Shuffle the data randomly
      const shuffledData = this.shuffleArray(data.results);
      
      // Slice the shuffled data to include any 4 random items
      this.accommodations = shuffledData.slice(0, 4);
      console.log(this.accommodations);
      this.loading = false;
    } catch (error) {
      console.error("Error fetching accommodations:", error);
      this.loading = false;
    }
  },
  shuffleArray(array) {
    // Function to shuffle array elements randomly
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
}
}
</script>

<style scoped>
.content-wrapper {
padding-top: 60px;
padding-bottom: 60px;
}

@media (min-width: 768px) {
.content-wrapper {
  padding-top: 100px;
  padding-bottom: 1px;
}
}

/* Style for the skeleton loading animation */
.animate-pulse {
animation: pulse 1.5s infinite ease-in-out;
}
@keyframes pulse {
0%, 100% {
  opacity: 0.4;
}
50% {
  opacity: 1;
}
}
</style>
