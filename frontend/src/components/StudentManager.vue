<!-- src/components/StudentManager.vue -->
<template>
    <div>
      <h2>Students</h2>
      <student-form @add-student="addStudent" />
      <div v-for="student in students" :key="student.id">
        <student-item :student="student" @remove="removeStudent(student.id)" />
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
  /* Your styles here */
  </style>
  