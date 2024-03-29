<template>
    <section class="py-16 md:py-20 lg:py-24 xl:py-32 bg-gray-200">
        <div class="container items-center max-w-6xl px-10 mx-auto sm:px-20 md:px-32 lg:px-16">
            <div class="flex flex-wrap ">
                <div class="order-1 w-full px-3 lg:w-1/2 lg:order-0">
                    <div class="w-full lg:max-w-md">
                        <h2 class="mb-4 text-3xl md:text-4xl lg:text-5xl font-bold leading-tight tracking-tight sm:text-4xl font-heading">
                            Why Choose Pillow.com?</h2>
                        <p class="mb-4 font-medium tracking-tight text-gray-600 lg:mb-6">Explore the benefits of
                            choosing Pillow.com for your student accommodation needs.</p>

                        <ul>
                            <li class="flex items-center py-2 space-x-4 xl:py-3">
                                <svg class="w-8 h-8 text-pink-500" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z">
                                    </path>
                                </svg>
                                <span class="font-medium text-gray-700">Accessible and efficient</span>
                            </li>
                            <li class="flex items-center py-2 space-x-4 xl:py-3">
                                <svg class="w-8 h-8 text-purple-500" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
                                </svg>
                                <span class="font-medium text-gray-700">Reliable student housing</span>
                            </li>
                            <li class="flex items-center py-2 space-x-4 xl:py-3">
                                <svg class="w-8 h-8 text-blue-500" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z">
                                    </path>
                                </svg>
                                <span class="font-medium text-gray-700">No login required.</span>
                            </li>
                        </ul>
                    </div>
                </div>
                <div
                    class="w-full px-3 mb-12 lg:w-1/2 order-0 lg:order-1 lg:mb-0"><img
                        class="mx-auto sm:max-w-sm lg:max-w-full"
                        src="https://cdn.devdojo.com/images/november2020/feature-graphic.png" alt="Feature Image">
                </div>
            </div>
        </div>
    </section>
    <footer class="bg-gray-900 text-white py-8">
        <div class="container mx-auto flex flex-col md:flex-row items-center justify-between px-4">
            <!-- Logo -->
            <div class="mb-4 md:mb-0 flex items-center">
                <img src="@/assets/logo.png" alt="Pillow Logo" class="h-8 w-auto mr-2">
                <div>
                    <h1 class="text-2xl font-bold inline-block">Pillow<span class="text-indigo-600">.com</span></h1>
                    <p class="text-sm">Discover comfortable and secure student accommodations near all three NWU Campuses.</p>
                </div>
            </div>
            
            
            
            <!-- Navigation -->
            <nav class="mb-4 md:mb-0">
                <ul class="flex space-x-4">
                    <li><a href="#" class="text-sm hover:text-indigo-600">Home</a></li>
                    <li><a href="#" class="text-sm hover:text-indigo-600">Accommodations</a></li>
                    <li><a href="#" class="text-sm hover:text-indigo-600">Ratings & Reviews</a></li>
                    <li><a href="#" class="text-sm hover:text-indigo-600">For Landlords</a></li>
                </ul>
            </nav>
            <!-- Social media links -->
            <div>
                <ul class="flex space-x-4">
                    <li><a href="#" class="text-sm hover:text-indigo-600"><i class="fab fa-facebook"></i></a></li>
                    <li><a href="#" class="text-sm hover:text-indigo-600"><i class="fab fa-twitter"></i></a></li>
                    <li><a href="#" class="text-sm hover:text-indigo-600"><i class="fab fa-instagram"></i></a></li>
                </ul>
            </div>
        </div>
    </footer>

  </template>
  
  <script>
  export default {
    name: 'Footer'
  }
  </script>
  
  <style scoped>
  /* Add any scoped styles here */
  </style>
  