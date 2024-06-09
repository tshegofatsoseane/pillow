<template>
    <nav class="nav">
      <ul class="nav__list">
        <li v-for="(tab, index) in tabs" :key="index" :class="{ 'nav__item': true, 'active-tab': activeTab === tab.name }">
          <a href="#" class="nav__link" @click.prevent="switchTab(tab.name)">{{ tab.name }}</a>
        </li>
      </ul>
      <div class="nav__slider" :style="{ transform: `translateX(${activeTabIndex * (100 / tabs.length)}%)` }">
        <div class="nav__slider-rect"></div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tabs: [
          { name: 'work', transform: 0 },
          { name: 'about', transform: 100 },
          { name: 'contacts', transform: 200 }
        ],
        activeTab: 'work'
      };
    },
    computed: {
      activeTabIndex() {
        return this.tabs.findIndex(tab => tab.name === this.activeTab);
      }
    },
    methods: {
      switchTab(tabName) {
        this.activeTab = tabName;
      }
    }
  }
  </script>
  
  <style scoped>
  /* Tailwind CSS styles for the navigation */
  .nav {
    width: 400px; /* Adjust the width as needed */
    height: 40px;
    border-radius: 15px;
    background-color: #E6F4F1;
    box-shadow: 2px 4px 6px rgba(0, 42, 50, 0.1);
    margin: 0 auto; /* Center the navigation bar horizontally */
  }
  
  .nav__list {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .nav__item {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .nav__link {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    color: #002A32;
    text-decoration: none;
    transition: color 0.3s ease-in-out;
  }
  
  .active-tab .nav__link {
    color: #ffffff;
    background-color: #00878E;
  }
  
  .nav__slider {
    position: relative;
    width: 100%;
    height: 95%;
    margin-top: -23px;
    padding: 3px;
    pointer-events: none;
    z-index: 0;
  }
  
  .nav__slider-rect {
    width: calc(100% / 3);
    height: 100%;
    background-color: #00878E;
    border-radius: 12px;
    transition: transform 0.4s;
    box-shadow: 1px 1px 3px rgba(0, 42, 50, 0.15);
  }
  </style>
  