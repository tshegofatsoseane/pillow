<template>
  <div v-if="isOpen" class="fixed top-0 left-0 w-full h-full flex justify-center items-center z-50">
    <!-- Dark transparent backdrop -->
    <div class="fixed top-0 left-0 w-full h-full bg-black opacity-50"></div>
    
    <!-- Popup content -->
    <div class="bg-white rounded-lg p-8 shadow-md">
      <!-- Your popup content here -->
      <div class="popup-inner">
        <!-- Popup content goes here -->
        <p>This is the map popup content.</p>
        <!-- Close button -->
        <button @click="closePopup" class="absolute top-0 right-0 mt-4 mr-4 text-gray-600 hover:text-gray-800 focus:outline-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M17.707 3.293a1 1 0 00-1.414 1.414L10 10.414l-6.293-6.293a1 1 0 00-1.414 1.414L8.586 12 2.293 18.293a1 1 0 101.414 1.414L10 13.414l6.293 6.293a1 1 0 001.414-1.414L11.414 12l6.293-6.293a1 1 0 000-1.414z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false
    };
  },
  methods: {
    closePopup() {
      this.$emit('close-popup');
    }
  }
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
