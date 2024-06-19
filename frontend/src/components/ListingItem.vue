<template>
    <div class="p-4 bg-gray-50 border rounded-lg shadow-sm flex justify-between items-center transform transition duration-300 hover:scale-105">
      <div>
        <h3 class="text-lg font-medium text-gray-800">{{ student.name }}</h3>
        <p class="text-gray-600">Email: {{ student.email }}</p>
      </div>
      <button @click="$emit('remove')" class="btn-danger">Remove</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StudentItem',
    props: {
      student: {
        type: Object,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .btn-danger {
    background-color: #ef4444;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.375rem;
    transition: background-color 0.3s;
  }
  
  .btn-danger:hover {
    background-color: #dc2626;
  }
  </style>
  