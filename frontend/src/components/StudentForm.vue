<template>
    <div>
      <h3 class="text-xl font-semibold text-gray-700 mb-2">Add New Student</h3>
      <form @submit.prevent="submitForm" class="space-y-4">
        <input v-model="name" placeholder="Name" class="input-field" required />
        <input v-model="email" type="email" placeholder="Email" class="input-field" required />
        <button type="submit" class="btn-primary">Add Student</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StudentForm',
    data() {
      return {
        name: '',
        email: ''
      };
    },
    methods: {
      submitForm() {
        const newStudent = {
          id: Date.now(),
          name: this.name,
          email: this.email
        };
        this.$emit('add-student', newStudent);
        this.name = '';
        this.email = '';
      }
    }
  }
  </script>
  
  <style scoped>
  .input-field {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #d1d5db;
    border-radius: 0.375rem;
    transition: border-color 0.3s;
  }
  
  .input-field:focus {
    outline: none;
    border-color: #6366f1;
  }
  
  .btn-primary {
    background-color: #4f46e5;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.375rem;
    transition: background-color 0.3s;
  }
  
  .btn-primary:hover {
    background-color: #4338ca;
  }
  </style>
  