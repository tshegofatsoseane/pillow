<template>
  <div class="content-wrapper">
    

    <div class="text-gray-500 py-14 mb-6 max-w-auto mx-auto" style="z-index: -10;">
      <div class="text-center ">
        <h1 class="text-4xl lg:text-4xl font-semibold mb-6 max-w-auto mx-auto">Featured accommodations in Potchefstroom</h1>
        <p hidden class="text-lg lg:text-xl mb-8 mx-auto">Discover comfortable and secure student accommodations near all NWU Campuses.</p>

        <div class="flex flex-wrap justify-center">
          <!-- Card 1 -->
          <div class="z-10 bg-white max-w-md mx-4 my-4 shadow-md rounded-xl relative"> <!-- Increased z-index -->
            <img class="w-full h-96 object-cover rounded-t-xl" src="https://helium.privateproperty.co.za/live-za-images/property/275/38/10176275/images/property-10176275-64564482_e.jpg" alt="Image">
            <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-gray-900 to-transparent h-80 rounded-b-xl"></div>
            <div class="absolute bottom-0 left-0 right-100 px-6 pb-6 text-white">
              <div class="font-bold text-xl right-100" style="margin-right: 105px;">SedibengVille</div>
              <p class="text-gray-200 text-base">
                Univeristy Drive, Unit 5, Mafikeng
              </p>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="z-10 bg-white max-w-md mx-4 my-4 shadow-md rounded-xl relative"> <!-- Increased z-index -->
            <img class="w-full h-96 object-cover rounded-t-xl" src="https://images.prop24.com/314970401/Crop600x400" alt="Image">
            <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-gray-900 to-transparent h-72 rounded-b-xl"></div>
            <div class="absolute bottom-0 left-0 right-100 px-6 pb-6 text-white">
              <div class="font-bold text-xl right-100" style="margin-right: 105px;">SedibengVille</div>
              <p class="text-gray-200 text-base">
                Univeristy Drive, Unit 5, Mafikeng
              </p>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="z-10 bg-white max-w-md mx-4 my-4 shadow-md rounded-xl relative"> <!-- Increased z-index -->
            <img class="w-full h-96 object-cover rounded-t-xl" src="https://images.prop24.com/314970401/Crop600x400" alt="Image">
            <div class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-gray-900 to-transparent h-72 rounded-b-xl"></div>
            <div class="absolute bottom-0 left-0 right-100 px-6 pb-6 text-white">
              <div class="font-bold text-xl right-100" style="margin-right: 105px;">SedibengVille</div>
              <p class="text-gray-200 text-base">
                Univeristy Drive, Unit 5, Mafikeng
              </p>
            </div>
          </div>

          <!-- Repeat the structure for the remaining cards -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hideNavbar: true
    }
  }
}
</script>

<style scoped>
/* Your scoped styles here */
</style>
