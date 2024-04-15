<template>
  <div class="detail-box md:mt-8 mt-14 md:p-6 rounded-lg md:shadow-lg bg-white" style="margin-top: -500px;">
    <!-- Image container -->
    <div class="md:flex">
      <div class="md:w-1/3 h-64 md:h-auto mb-6 md:mb-0 md:mr-6">
        <img :src="image_url" alt="Author Photo" class="object-cover w-full h-full rounded-lg" style="width: 500px;">
      </div>

      <!-- Details section -->
      <div class="md:w-2/3">
        <!-- Tags -->
        <div class="flex flex-wrap space-x-2 mb-4">
          <span class="tag bg-blue-600 border border-blue-600 ">Mafikeng</span>
          <span class="tag bg-blue-600 border border-blue-600">Accredited</span>
          <button @click="openModal" class="px-3 py-1 text-sm font-semibold border shadow-lg border-blue-600 text-blue-600 bg-white rounded-full flex items-center transition duration-300 ease-in-out hover:bg-blue-800 hover:text-white hover:translate-y-[-2px]">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 2a7 7 0 00-7 7c0 5.25 7 11 7 11s7-5.75 7-11a7 7 0 00-7-7zm0 9a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
            </svg>
            Take me there
          </button>
        </div>

        <!-- Modal component -->
        <div v-if="isModalOpen" class="fixed inset-0 z-10 overflow-y-auto flex items-center justify-center">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" @click="closeModal"></div>
          <div class="relative bg-white rounded-lg max-w-2xl p-8" style="width: 1000px; height: 800px">
            <!-- Modal content -->
            <h2 class="text-xl font-semibold mb-4">Popup Modal Title</h2>
            <p class="text-gray-700 mb-4">Popup Modal Content</p>
            <!-- Street View iframe -->
            <iframe v-if="streetViewUrl" class="w-full" style="min-height: 300px;" frameborder="0" :src="streetview_url" allowfullscreen></iframe>
            <!-- Directions iframe -->
            <iframe v-if="directionsUrl" class="w-full" style="min-height: 300px;" frameborder="0" :src="directionsUrl" allowfullscreen></iframe>
            <button @click.self="closeModal" class="action-button bg-indigo-500 text-white">Close</button>
          </div>
        </div>

        <!-- Ratings -->
        <div class="flex items-center mb-4">
          <span class="text-xl font-semibold text-yellow-500 mr-2">★★★★★</span>
          <span class="text-gray-600">(25 Reviews)</span>
        </div>

        <!-- Title -->
        <h2 class="text-2xl text-left text-gray-500 font-bold mb-4">{{ residence_name }}</h2>

        <!-- Description -->
        <div class="mb-4">
          <p class="font-medium text-gray-500 text-left text-lg "> <span class="text-black">Address: </span> {{ street_address }}</p>
          <p class="font-medium text-gray-500 text-left text-lg "> <span class="text-black">Nearest campus: </span> {{ nearest_campus }}</p>
          <p class="font-medium text-gray-500 text-left text-lg"><span class="text-black">Email: </span>{{ email }}</p>
          <p class="font-medium text-gray-500 text-left text-lg"><span class="text-black">Phone number: </span>{{ cell_number }}</p>
        </div>

        <!-- Action buttons -->
        <div class="flex mb-6">
          <button class="action-button bg-white border border-blue-600 text-blue-600 mr-4 flex items-center hover:bg-green-500 hover:border-green-500 hover:text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mr-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 4v7m0 0v4m0-4h6a2 2 0 002-2V6a2 2 0 00-2-2h-6a2 2 0 00-2 2z"></path>
            </svg>
            Call
          </button>
          <button class="action-button bg-white border border-blue-600 text-blue-600 flex items-center  hover:bg-red-500 hover:border-red-500 hover:text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mr-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 12h-6l-6 8H8l-6-8h6l6-8h4l6 8z"></path>
            </svg>
            Email
          </button>
        </div>

        <div class=" w-full border-t border-gray-300"></div>
      </div>
    </div>

    <!-- Review section -->
    <div class="mt-8">
      <h2 class="text-2xl text-left font-semibold mb-4">Reviews</h2>
      <div v-for="review in reviews" :key="review.id" class="mb-4">
        <div class="flex items-start">
          <div class="mt-1">
            <div v-for="review in reviews" :key="review.id" class="mb-4">
              <div class="flex items-start">
                <!-- User avatar -->
                <div class="mr-4">
                  <div class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center">
                    <span class="text-gray-600">{{ review.user.charAt(0).toUpperCase() }}</span>
                  </div>
                </div>
                <!-- User name, ratings, and review -->
                <div class="mb-2">
                  <!-- User name and ratings -->
                  <div class="flex items-center mb-">
                    <p class="font-semibold mr-2">{{ review.user }}</p>
                    <span class="text-lg font-semibold text-yellow-500 mr-2">★★★</span>
                  </div>
                  <!-- Review text -->
                  <div>
                    <div class=" w-full border-t border-gray-300 mb-2"></div>
                    <p class="text-gray-700 text-left">{{ review.text }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Review form -->
      <div class="mt-8">
        <h2 class="text-2xl text-left font-semibold mb-4">Leave a Review</h2>
        <form @submit.prevent="addreview" class="flex flex-col md:flex-row">
          <textarea v-model="newreview.text" rows="1" class="flex-1 mr-0 md:mr-4 mb-4 md:mb-0 p-4 rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter your review"></textarea>
          <button type="submit" class="action-button bg-blue-600 text-white">Add Review</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import MapPopup from '@/components/MapPopup.vue'; 
export default {
  name: 'DetailBox',
  components: {
    MapPopup
  },
  data() {
    return {
      isModalOpen: false,
      streetViewUrl: 'https://www.google.com/maps/@?api=1&map_action=streetview&pano=-25.8388141%2C25.6184332&viewpoint=-25.8388141%2C25.6184332',
      directionsUrl: 'https://www.google.com/maps/dir/?api=1&destination=-25.8388141,25.6184332&key=AIzaSyD9dGsjV6QwyIZEubLJsdgNe6dldKH-6dU',
      streetAddress: 'KGALEGI CRESCENT STREET 2243 MONTSHIOA UNIT 1 MMABATHO', // Initialize with empty string or set it from external source
      loading: false,
      reviews: [
        { id: 1, user: 'Mmathapelo', text: 'Great residence. Lovely landlord' },
      ],
      newreview: {
        user: 'You', // You can set the user dynamically or fetch it from the logged-in user
        text: ''
      }
    };
  },
  props: {
    routeParams: {
      type: Object,
      default: () => ({})
    }
  },
  computed: {
    residence_name() {
      return this.$route.query.residence_name;
    },
    id() {
      return this.$route.params.id;
    },
    image_url() {
      return this.$route.query.image_url;
    },
    street_address() {
      return this.$route.query.street_address;
    },
    streetview_url() {
      return this.$route.query.streetview_url;
    },
    nearest_campus() {
      return this.$route.query.nearest_campus; 
    },
    cell_number() {
      return this.$route.query.cell_number; 
    },
    email() {
      return this.$route.query.email; 
    }
  },
  mounted() {
    window.scrollTo(0, 0);
    this.streetAddress = this.$route.query.street_address;
  },
  methods: {
    openModal() {
      // Fetch street view and directions URLs
      this.fetchStreetView();
      this.fetchDirections();
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    fetchStreetView() {
  // Construct street view URL based on street address
  const encodedAddress = encodeURIComponent(this.streetAddress);
  this.streetViewUrl = `https://www.google.com/maps/embed/v1/streetview?key=YOUR_API_KEY&location=${encodedAddress}`;
},

fetchDirections() {
  // Construct directions URL based on street address and user's current location as origin
  const encodedAddress = encodeURIComponent(this.streetAddress);
  const origin = encodeURIComponent('4040 Peace CrescentMmabatho Unit 12, Mmabatho, 2790'); // Replace 'CURRENT_LOCATION' with actual user's current location
  this.directionsUrl = `https://www.google.com/maps/embed/v1/directions?key=AIzaSyD9dGsjV6QwyIZEubLJsdgNe6dldKH-6dU&origin=${origin}&destination=${encodedAddress}`;
},

    addreview() {
      if (this.newreview.text.trim() !== '') {
        this.reviews.push({
          id: this.reviews.length + 1,
          user: this.newreview.user,
          text: this.newreview.text
        });
        this.newreview.text = '';
      }
    }
  },
};
</script>

<style scoped>
.detail-box {
  transition: all 0.3s ease;
}

.tag {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: #ffffff;

  border-radius: 999px;
}

.action-button {
  padding: 0.4rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 999px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.action-button:hover {
  transform: translateY(-2px);
}
</style>
