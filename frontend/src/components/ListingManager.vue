<template>
    <div class="bg-white shadow-lg rounded-lg p-6">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">Students</h2>
      <student-form @add-student="addStudent" />
      <div class="space-y-4 mt-4">
        <student-item v-for="student in students" :key="student.id" :student="student" @remove="removeStudent(student.id)" />
      </div>
    </div>
  </template>
  
  <script>
  import StudentForm from './StudentForm.vue'
  import StudentItem from './StudentItem.vue'
  
  export default {
    name: 'StudentManager',
    components: {
      StudentForm,
      StudentItem
    },
    props: {
      students: {
        type: Array,
        required: true
      }
    },
    methods: {
      addStudent(newStudent) {
        this.$emit('update:students', [...this.students, newStudent]);
      },
      removeStudent(id) {
        this.$emit('update:students', this.students.filter(student => student.id !== id));
      }
    }
  }
  </script>
  
  <style scoped>
  /* Additional styles if needed */
  </style>
  