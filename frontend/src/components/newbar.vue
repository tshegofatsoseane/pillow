<template>
  <div>
    <nav
      id="nav-bar"
      :class="['nav', isScrolled ? 'nav-bar-scrolled' : 'nav-bar-top']"
      @scroll="handleScroll"
    >
    <div class="wrapper flex justify-between items-center z-50" style="margin-top: -15px;">
        <!-- Logo -->
        <div class="flex items-center ml-6">
          <img src="@/assets/logo.png" alt="Pillow Logo" class="h-8 w-auto mr-2" />
          <div class="text-2xl font-bold border-white rounded-full" :class="{ 'text-indigo-500': isScrolled }">Pillow</div>
        </div>

        <input type="checkbox" id="menu-toggle" class="hidden">
        <label for="menu-toggle" class="label-toggle hamburger"></label>

        <ul class="menu-list flex justify-around items-center">
          <!-- Navigation Links -->
          <div class="nav-wrapper" style="margin-top: -2px; margin-left: 520px;">

          </div>
        </ul>


<!-- Center Search Box -->
<div class="flex justify-center items-center mt-2 mr-80" v-if="showSearchInput">
  <div class="flex items-center bg-white border border-gray-300 rounded-full shadow-sm px-4 py-2 space-x-4" style="height: 45px;">
    <!-- University button -->
    <button 
      class="focus:outline-none text-black font-semibold relative"
      @click="toggleUniversityDropdown"
    >
      University
      <div v-if="showUniversityDropdown" class="absolute bg-white border border-gray-300 rounded shadow-lg mt-4 w-64 p-4 grid grid-cols-2 gap-4">
        <a href="#" class="block text-center">
          <div class="bg-gray-200 p-4 rounded-md">
            <span>NWU</span>
          </div>
        </a>
        <a href="#" class="block text-center">
          <div class="bg-gray-200 p-4 rounded-md">
            <span>UJ</span>
          </div>
        </a>
        <a href="#" class="block text-center">
          <div class="bg-gray-200 p-4 rounded-md">
            <span>UFS</span>
          </div>
        </a>
        <a href="#" class="block text-center">
          <div class="bg-gray-200 p-4 rounded-md">
            <span>WITS</span>
          </div>
        </a>
      </div>
    </button>

    <!-- Divider -->
    <div class="border-l h-6"></div>

    <!-- Add guests button -->
    <button class="focus:outline-none text-gray-500">
      Campus
    </button>

    <!-- Search Icon button -->
    <button class="bg-indigo-500 rounded-full p-2 focus:outline-none">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M12.9 14.32A8 8 0 1114.32 12.9l4.387 4.386a1 1 0 11-1.414 1.414l-4.386-4.387zM8 14A6 6 0 108 2a6 6 0 000 12z" clip-rule="evenodd" />
      </svg>
    </button>
  </div>
</div>



        <div :class="{ 'hidden': !showMenu, 'lg:flex': showMenu }" class="lg:flex hover:border-white">
              <router-link hidden to="/" class="font-semibold px-4 py-4 transition duration-700 ease-in-out text-gray-500 hover:text-indigo-700 hover:border-blue-500" :class="{ 'border-b-2 border-blue-500': $route.path === '/', 'text-gray-500 border-indigo-500': isScrolled }">Home</router-link>
              <router-link :to="{ name: 'landlord-dashboard' }" class="font-semibold px-4 py-4 transition duration-300 text-gray-500 ease-in-out hover:text-indigo-700 hover:border-blue-500 overflow-hidden whitespace-nowrap" :class="{ 'border-b-2 border-blue-500': $route.name === 'landlord-dashboard', 'text-gray-500 border-indigo-400 mr-22': isScrolled }">For Landlords</router-link>
            </div>
        <!-- Action Buttons -->
              <div
              
        class="flex items-center justify-center py-2 px-4 mr-10 bg-white border border-gray-300 text-gray-600 rounded-full hover:bg-gray-100 transition duration-300 relative"
        style="width: 120px; height: 40px;"
      >

        <!-- Hamburger Icon -->
        <i class="bi bi-list text-xl cursor-pointer pr-2 hover:text-indigo-500"></i>

        <!-- Person Icon with Dropdown Menu -->
        <i
          class="bi bi-person text-xl cursor-pointer hover:text-indigo-500"
          @mouseover="showDropdown = true"
          @mouseleave="showDropdown = false"
        ></i>

        <!-- Dropdown Menu -->
        <div
          v-if="showDropdown"
          class="absolute top-full right-0 mt-2 bg-white border rounded shadow-lg p-2"
        >
          <router-link
            :to="{ name: 'login' }"
            class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
            >Login</router-link
          >
          <router-link
            :to="{ name: 'signup' }"
            class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
            >Signup</router-link
          >
        </div>
      </div>
      </div>
      <div v-if="isScrolled" class="separator"></div>

      <!-- Show Filters and Toggle only if scrolled -->
      <div v-if="isScrolled" class="flex items-center space-x-6 py-4 mx-5 text-xs font-bold">
        <!-- Search Section -->
        <div class="flex flex-col items-center">
          <i class="bi bi-house-door text-xl text-indigo-400"></i>
          <span class="ml-2">Your search</span>
        </div>

        <!-- Icons with text -->
        <div class="flex items-center space-x-6">
          <div v-for="item in menuItems" :key="item.label" class="flex flex-col items-center">
            <i :class="`bi bi-${item.icon} font-bold text-gray-600 text-xl`"></i>
            <span class="text-xs text-gray-500 font-bold">{{ item.label }}</span>
          </div>
        </div>

        <!-- Filters and Toggle -->
        <div class="flex items-center space-x-4 ml-auto" style="margin-left: 295px;">
          <button class="bg-gray-200 px-3 py-2 rounded-md text-xs font-bold">Filters</button>
          <div class="flex items-center space-x-2">
            <span class="text-xs font-bold">Display total before taxes</span>
            <label class="switch">
              <input type="checkbox" v-model="toggle">
              <span class="slider"></span>
            </label>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isScrolled: false,
      showSearchInput: false,
      searchQuery: '',
      toggle: false,
      showDropdown: false,
      showUniversityDropdown: false,
      menuItems: [
        { icon: 'building', label: 'Shared Flats' },
        { icon: 'house', label: 'House Rentals' },
        { icon: 'tree', label: 'Green Spaces' },
        { icon: 'bicycle', label: 'Bike-Friendly' },
        { icon: 'house', label: 'Near Amenities' },
        { icon: 'wifi', label: 'High-Speed Internet' },
        { icon: 'lock', label: 'Secure Access' },
      ],
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    document.addEventListener('click', this.handleOutsideClick);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
    document.removeEventListener('click', this.handleOutsideClick);
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 0;
      const scrollPosition = window.scrollY;
      const windowHeight = window.innerHeight;
      const fullHeight = document.body.scrollHeight;
      const middleScrollPosition = (fullHeight - windowHeight) / 100;
      this.showSearchInput = scrollPosition >= middleScrollPosition;
    },
    toggleUniversityDropdown(event) {
      event.stopPropagation(); // Prevents the click event from propagating to document
      this.showUniversityDropdown = !this.showUniversityDropdown;
    },
    handleOutsideClick(event) {
      const dropdown = this.$el.querySelector('div.absolute');
      if (dropdown && !dropdown.contains(event.target)) {
        this.showUniversityDropdown = false;
      }
    },
    handleSearch() {
      console.log('Search query:', this.searchQuery);
    },
  }
};
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css?family=Mada:400,500';
@import 'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.10.3/font/bootstrap-icons.min.css';

.nav {
  height: 65px;
  transition: width 0.2s ease-in-out;
  margin-top: -15px;
  background-color: #fff;
  border-radius: 30px;
  z-index: 1000;
}

.nav-bar-top {
  width: 70%;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 60px;
}

.nav-bar-scrolled {
  position: fixed;
  width: 100%;
  left: 50%;
  top: 0;
  transform: translateX(-50%);
  border-radius: 1px;
  height: 100px;
  transition: height 0.3s ease-in-out;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  height: 170px;
}

.separator {
  height: 2px;
  background: whitesmoke;
  border-radius: 50px;
  margin-top: -20px;
}

.menu-list {
  display: flex;
  width: 65%;
  justify-content: space-around;
  align-items: center;
  list-style: none;
  margin: 0 auto;
  height: 90px;
  text-decoration: none;
  padding: 0;
}

.nav-link {
  letter-spacing: 0.15em;
  font-size: 1em;
  color: #1b1b1b;
  font-weight: 500;
  text-decoration: none;
}

.nav-link:hover {
  color: #e0696c;
}

.label-toggle {
  display: none;
}

.nav-bar-scrolled .menu-list {
  display: flex;
  width: 65%;
  justify-content: space-around;
  align-items: center;
  list-style: none;
  margin: 0 auto;
  height: 100px;
  text-decoration: none;
  padding: 0;
  margin-left: 10px;
  margin-top: 25px;
}

.nav-bar-scrolled .nav-wrapper {
  margin-top: -100px;
  overflow: hidden;
  white-space: nowrap;;
}

.wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  
}

/* Center the search box properly within the navbar */
.searchbox-container {
  flex: 1; /* This makes the search box container take available space */
  display: flex;
  justify-content: center; /* Center the search box horizontally */
  align-items: center;
  margin: 0 auto; /* Optional: ensures it's centered within the available space */

}

/* Search input styling */
.search-input {
  padding: 0.75rem 1rem;
  border: 1px solid #9ca3af;
  border-radius: 0.5rem;
  width: 300px;
  max-width: 100%;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: indigo;
}



button:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.2);
}

button:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

div.border-l {
  border-left-width: 1px;
  border-color: #e2e8f0;
}

@media screen and (max-width: 961px) {
  .nav {
    width: 100%;
    position: fixed;
    top: 0;
  }
}

@media screen and (max-width: 768px) {
  .wrapper {
    padding: 0;
  }

  .nav-logo {
    top: 10px;
    position: absolute;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
  }

  .label-toggle {
    cursor: pointer;
  }

  .menu-list:last-of-type {
    border-bottom: 2px solid #e0696c;
  }

  #menu-toggle:checked ~ .menu-list {
    opacity: 1;
    height: auto;
    visibility: visible;
  }

  .label-toggle {
    display: block;
    height: 35px;
    margin-top: 27.5px;
    width: 35px;
    top: 0;
    position: absolute;
    right: 20px;
  }
}

.switch {
  position: relative;
  display: inline-block;
  width: 34px;
  height: 20px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 20px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 12px;
  width: 12px;
  border-radius: 50%;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
}

input:checked + .slider {
  background-color: #4CAF50;
}

input:checked + .slider:before {
  transform: translateX(14px);
}

/* Dropdown Menu Styles */
.dropdown-menu {
  display: none;
}

.dropdown-menu.visible {
  display: block;
}

.dropdown-menu a {
  text-decoration: none;
  color: #333;
}

.dropdown-menu a:hover {
  background-color: #f0f0f0;
}

/* Dropdown Menu Styles */
.relative {
  position: relative;
}

.absolute {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
}

.dropdown-menu a {
  text-decoration: none;
  color: #333;
}

.dropdown-menu a:hover {
  background-color: #f0f0f0;
}


</style>
