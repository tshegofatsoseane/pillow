<template>
    <div>
      <h3 class="text-xl font-semibold text-gray-700 mb-2">Add New Listing</h3>
      <form @submit.prevent="submitForm" class="space-y-4">
        <input v-model="title" placeholder="Title" class="input-field" required />
        <input v-model="location" placeholder="Location" class="input-field" required />
        <input v-model="price" type="number" placeholder="Price" class="input-field" required />
        <button type="submit" class="btn-primary">Add Listing</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AccommodationForm',
    data() {
      return {
        title: '',
        location: '',
        price: ''
      };
    },
    methods: {
      submitForm() {
        const newListing = {
          id: Date.now(),
          title: this.title,
          location: this.location,
          price: parseFloat(this.price)
        };
        this.$emit('add-listing', newListing);
        this.title = '';
        this.location = '';
        this.price = '';
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
  