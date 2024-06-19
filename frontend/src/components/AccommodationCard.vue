<!-- src/components/AccommodationCard.vue -->
<template>
    <div class="accommodation-card bg-white rounded-7xl cursor-pointer rounded-b-3xl overflow-hidden shadow-lg transition duration-300 transform hover:shadow-xl">
      <img :src="accommodation.image_url" alt="Accommodation Image" class="w-full h-60 object-cover rounded-t-3xl" />
  
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
        <router-link :to="detailsLink" class="bottom-4 py-2 my-2 left-2 w-28 h-10 flex items-center justify-center bg-white border border-black text-black rounded-full hover:bg-gray-700 transition duration-300">
          View details
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AccommodationCard',
    props: {
      accommodation: {
        type: Object,
        required: true
      }
    },
    computed: {
      detailsLink() {
        return {
          name: 'details',
          params: { id: this.accommodation.id },
          query: {
            residence_name: this.accommodation.residence_name,
            image_url: this.accommodation.image_url,
            street_address: this.accommodation.street_address,
            nearest_campus: this.accommodation.nearest_campus,
            cell_number: this.accommodation.cell_number,
            email: this.accommodation.email,
            map_url: this.accommodation.map_url,
            directions_url: this.accommodation.directions_url,
            streetview_url: this.accommodation.streetview_url
          }
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .accommodation-card {
    width: 20rem;
  }
  </style>
  