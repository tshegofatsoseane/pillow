<template>
  <div class="search-box-wrapper shadow-2xl shadow-indigo-400 border p-6 mt-20 rounded-3xl">
    <!-- Large box with gray background and rounded corners -->
    <div class="flex flex-col md:flex-row">
      <!-- Image container -->
      <div class="bg-gray-100 w-full md:w-98 h-96 rounded-3xl flex items-center justify-center" >
          <img src="https://helium.privateproperty.co.za/live-za-images/property/275/38/10176275/images/property-10176275-64564482_e.jpg" alt="Author Photo" class="object-cover w-full h-full rounded-2xl" >
        </div>


      <!-- Details and review section container -->
      <div class="mt-6 md:mt-0 md:ml-4 flex flex-col w-full">
        <!-- Details -->
        <div class="bg-white rounded-xl p-6 mb-6">
          <div class="flex flex-col md:flex-row md:items-center space-y-4 md:space-y-0 md:space-x-4 mb-4">
            <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Mafikeng</span>
            <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Accredited</span>
            <span class="inline-block px-3 py-1 text-sm font-semibold text-white bg-indigo-500 rounded-full">Tag #3</span>
          </div>
          <!-- Title -->
          <div class=" text-left">
            <h2 class="text-2xl pb-4 font-bold text-black ">SedibengVille</h2>
          </div>
          <!-- Description -->
          <div class="text-left">
            <h1 class=" font-medium mb-1 text-black"> Univeristy Drive, Unit 5, Mafikeng</h1>
          </div>
          <!-- Description -->
          <div class="text-left ">
            <p class=" font-medium mb-1 text-black"> Nearest campus: Mafikeng</p>
          </div>
          <!-- Description -->
          <div class="text-left ">
            <p class=" font-medium mb-1 text-black"> Number of beds: 7</p>
          </div>
          <!-- Description -->
          <div class="text-left ">
            <p class=" font-medium mb-1 text-black"> Email: sedibeng@gmail.com</p>
          </div>
          <!-- Description -->
          <div class="text-left pb-6">
            <p class=" font-medium text-black"> Phone number: 0832763723</p>
          </div>
          <div class="w-full md:w-1/4 border-t border-gray-300 md:hidden"></div> <!-- Display border on small screens -->
          <!-- Read more and Author section -->
          <div class="flex items-center justify-between mt-4">
            <router-link :to="{ name: 'details' }" class="px-4 py-4 transition duration-300 ease-in-out text-blue-600 dark:text-blue-400 hover:underline">Details ⟶</router-link>
            <div class="flex items-center">
              <a class="font-bold text-black cursor-pointer">John Doe</a>
            </div>
          </div>
        </div>

        <!-- review section -->
        <div class="bg-white rounded-xl p-6 overflow-y-auto" style="margin-top: -110px;">
          <h2 class="text-lg font-semibold mb-4 text-left">Reviews</h2>
          <!-- Add review section content here -->
          <div v-for="review in reviews" :key="review.id" class="mb-4">
            <div class="flex items-start">
              <p class="font-semibold text-gray-800 mr-2">{{ review.user }}:</p>
              <p class="text-gray-700">{{ review.text }}</p>
            </div>
          </div>
          <br>

          <div class="w-1/4 md:w-full border-t border-gray-300"></div>
          <br>
          <!-- Review form -->
          <h2 class="text-3xl font-semibold mb-4 text-left">Leave a Review</h2>
          <form @submit.prevent="addreview" class="mt-6 flex flex-col md:flex-row">
            <!-- Textarea for review -->
            <textarea v-model="newreview.text" rows="2" class="flex-1 mr-0 md:mr-2 mb-4 md:mb-0 px-4 py-2 shadow-md rounded-md border-gray-600 focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter your review"></textarea>
            <!-- Submit button with send icon -->
            <button type="submit" class="px-4 py-2 bg-indigo-500 text-white rounded-md hover:bg-indigo-600 focus:outline-none focus:bg-indigo-600 flex items-center w-full md:w-auto">
              <!-- Send icon -->
              <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              <!-- Text on the button -->
              Add Review
            </button>
          </form>

          <!-- Ratings section -->
          <div class="flex items-center mt-4">
            <span class="text-xl font-semibold text-yellow-500">★★★★★</span>
            <span class="ml-2 text-gray-600">(25 Reviews)</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DetailBox',
  data() {
    return {
      loading: false,
      reviews: [
        { id: 1, user: 'User 1', text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' },
      ],
      newreview: {
        user: 'You', // You can set the user dynamically or fetch it from the logged-in user
        text: ''
      }
    };
  },
  methods: {
    submit() {
      // Simulate loading for 2 seconds
      this.loading = true;
      setTimeout(() => {
        this.loading = false;
        this.showResults = true;
        this.$emit('search-submitted');

        // Scroll to the top of the page
        window.scrollTo({
          top: 0,
          behavior: 'smooth', // Optional: smooth scrolling effect
        });
      }, 2000);
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
/* Add any scoped styles here */
</style>
