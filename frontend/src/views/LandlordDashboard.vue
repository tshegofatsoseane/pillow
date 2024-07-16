<template>
    <div class="flex h-screen  bg-gray-100 font-poppins">
      <!-- Sidebar -->
      <SideNav />
  
      <!-- Main Content -->
      <main class="flex-1 p-6 overflow-y-auto">
        <!-- Header -->
        <header class="flex items-center justify-between mb-6">
          <h1 class="text-3xl font-bold text-indigo-900">Landlord Dashboard</h1>
          <button class="flex items-center bg-indigo-900 hover:bg-indigo-800 text-white py-2 px-4 rounded-lg shadow-md transition duration-300">
            <i class='bx bx-plus mr-2'></i>
            Add New Student
          </button>
        </header>
  
        <!-- Dashboard Overview -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
          <!-- Students Card -->
          <div class="bg-white p-6 rounded-lg shadow-md flex items-center justify-between">
            <div>
              <h2 class="text-lg font-semibold text-gray-700">Total Students</h2>
              <p class="text-3xl font-bold text-indigo-600">25</p>
            </div>
            <i class='bx bx-user text-indigo-600 text-5xl'></i>
          </div>

          <!-- Accommodations Card -->
          <div class="bg-white p-6 rounded-lg shadow-md flex items-center justify-between">
            <div>
              <h2 class="text-lg font-semibold text-gray-700">Total Accommodations</h2>
              <p class="text-3xl font-bold text-indigo-600">12</p>
            </div>
            <i class='bx bx-home text-indigo-600 text-5xl'></i>
          </div>

          <!-- Occupancy Rate Card -->
          <div class="bg-white p-6 rounded-lg shadow-md flex items-center justify-between">
            <div>
              <h2 class="text-lg font-semibold text-gray-700">Occupancy Rate</h2>
              <p class="text-3xl font-bold text-indigo-600">85%</p>
            </div>
            <i class='bx bx-bar-chart-alt-2 text-indigo-600 text-5xl'></i>
          </div>

          <!-- Revenue Card -->
          <div class="bg-white p-6 rounded-lg shadow-md flex items-center justify-between">
            <div>
              <h2 class="text-lg font-semibold text-gray-700">Total Revenue</h2>
              <p class="text-3xl font-bold text-indigo-600">$12,500</p>
            </div>
            <i class='bx bx-dollar-circle text-indigo-600 text-5xl'></i>
          </div>
        </section>
  
        <!-- Students Table -->
        <section class="mb-6">
          <h2 class="text-2xl font-semibold text-indigo-900 mb-4">Students</h2>
          <div class="bg-white rounded-lg shadow-md overflow-hidden">
            <table class="w-full">
              <thead class="bg-indigo-500 text-white">
                <tr>
                  <th class="py-3 px-4 text-left">Name</th>
                  <th class="py-3 px-4 text-left">Email</th>
                  <th class="py-3 px-4 text-left">Phone</th>
                  <th class="py-3 px-4 text-left">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(student, index) in students" :key="index" class="border-t hover:bg-gray-100 transition duration-300">
                  <td class="py-4 px-6">{{ student.name }}</td>
                  <td class="py-4 px-6">{{ student.email }}</td>
                  <td class="py-4 px-6">{{ student.phone }}</td>
                  <td class="py-4 px-6">
                    <button class="text-indigo-600 hover:text-indigo-800 focus:outline-none">
                      <i class='bx bx-edit'></i>
                    </button>
                    <button class="text-red-600 hover:text-red-800 focus:outline-none ml-2">
                      <i class='bx bx-trash'></i>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
  
        <!-- Accommodations Table -->
        <section>
          <h2 class="text-2xl font-semibold text-indigo-900 mb-4">Accommodations</h2>
          <div class="bg-white rounded-lg shadow-md overflow-hidden">
            <table class="w-full">
              <thead class="bg-indigo-500 text-white">
                <tr>
                  <th class="py-3 px-4 text-left">Name</th>
                  <th class="py-3 px-4 text-left">Description</th>
                  <th class="py-3 px-4 text-left">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(accommodation, index) in accommodations" :key="index" class="border-t hover:bg-gray-100 transition duration-300">
                  <td class="py-4 px-6">{{ accommodation.name }}</td>
                  <td class="py-4 px-6">{{ accommodation.description }}</td>
                  <td class="py-4 px-6">
                    <button class="text-indigo-600 hover:text-indigo-800 focus:outline-none">
                      <i class='bx bx-edit'></i>
                    </button>
                    <button class="text-red-600 hover:text-red-800 focus:outline-none ml-2">
                      <i class='bx bx-trash'></i>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  </template>
  
  <script>
  import SideNav from '@/components/SideNav.vue'
  
  export default {
    components: {
      SideNav
    },
    name: 'LandlordDashboard',
    data() {
      return {
        students: [
          { name: 'John Doe', email: 'john.doe@example.com', phone: '+1234567890' },
          { name: 'Jane Smith', email: 'jane.smith@example.com', phone: '+9876543210' },
          // Add more student objects as needed
        ],
        accommodations: [
          { name: 'Apartment 1', description: 'Beautiful apartment in downtown.' },
          { name: 'House 3', description: 'Spacious house with a garden.' },
          // Add more accommodation objects as needed
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  @import url('https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css');
  
  .font-poppins {
    font-family: 'Poppins', sans-serif;
  }
  </style>
  