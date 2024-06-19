<!-- src/components/StudentItem.vue -->
<template>
    <div class="student-item">
      <h3>{{ student.name }}</h3>
      <p>Email: {{ student.email }}</p>
      <button @click="$emit('remove')">Remove</button>
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
  /* Your styles here */
  </style>
  