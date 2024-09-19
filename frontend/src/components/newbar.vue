<template>
  <div>
    <nav
      id="nav-bar"
      :class="['nav', isScrolled ? 'nav-bar-scrolled' : 'nav-bar-top']"
      @scroll="handleScroll"
    >
    
    
      <div class="wrapper flex justify-between items-center z-50 " style="margin-top: -15px;">
        <!-- Logo -->
        <div class="flex items-center ml-6">
          <img src="@/assets/logo.png" alt="Pillow Logo" class="h-8 w-auto mr-2">
          <div class="text-2xl font-bold border-white rounded-full " :class="{ 'text-indigo-500': isScrolled }">Pillow</div>
        </div>

        <input type="checkbox" id="menu-toggle" class="hidden">
        <label for="menu-toggle" class="label-toggle hamburger"></label>

        <ul class="menu-list flex justify-around items-center" >
          <!-- Navigation Links -->
          <div class="nav-wrapper" style="margin-top: -2px;">
            <div :class="{ 'hidden': !showMenu, 'lg:flex': showMenu }" class="lg:flex hover:border-white">
            <router-link to="/" class="font-semibold px-4 py-4 transition duration-700 ease-in-out text-gray-500 hover:text-indigo-700 hover:border-blue-500" :class="{ 'border-b-2 border-blue-500': $route.path === '/', 'text-gray-500 border-indigo-500': isScrolled }">Home</router-link>
            <router-link :to="{ name: 'landlord-dashboard' }" class="font-semibold px-4 py-4 transition duration-300 text-gray-500 ease-in-out hover:text-indigo-700 hover:border-blue-500" :class="{ 'border-b-2 border-blue-500': $route.name === 'landlord-dashboard', 'text-gray-500 border-indigo-400': isScrolled }">For Landlords</router-link>
          </div>
          </div>
        </ul>

        <div class="searchbox">
            <!-- Search Form -->
            <form @submit.prevent="handleSearch" class="relative flex-grow mb-4" v-if="showSearchInput">
              <input v-model="searchQuery" type="text" class="search-input" placeholder="Enter your search...">
              <button type="submit" class="search-icon">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </button>
            </form>

          </div>


        <!-- Action Buttons -->
        <div class="mr-12 flex items-center space-x-4">
          <router-link :to="{ name: 'innovation' }" class="border border-indigo-500 text-gray-500 font-semibold py-2 px-6 rounded transition duration-300 ease-in-out hover:text-indigo-500 hover:border-indigo-800">Login</router-link>
          <router-link :to="{ name: 'signup' }" class=" bg-indigo-600/90 to-pink-800/50 hover:bg-indigo-600/60 text-white font-semibold py-2 px-6 rounded transition duration-300 ease-in-out">Signup</router-link>
        </div>
      </div>
      <div v-if="isScrolled" class="separator"></div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isScrolled: false,
      showSearchInput: false,
      searchQuery: ''
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 0;

      // calculate scroll position to trigger showing the search input
      const scrollPosition = window.scrollY;
      const windowHeight = window.innerHeight;
      const fullHeight = document.body.scrollHeight;

     //show search input when scroll is in the middle 50% of the page 
      const middleScrollPosition = (fullHeight - windowHeight) / 9;

      this.showSearchInput = scrollPosition >= middleScrollPosition;
    },
    handleSearch() {
      console.log('Search query:', this.searchQuery);

    }
  }
};
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css?family=Mada:400,500';

.nav {
  height: 65px;
  transition: width 0.2s ease-in-out;
  margin-top: -15px;
  background-color: #fff;
  border-radius: 30px;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.1);
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
  height: 100px; /* Adjusted height when scrolled */
  transition: height 0.3s ease-in-out; /* Smooth transition */
  border-bottom: 1px solid #e5e7eb; /* Existing bottom border */
  display: flex;
  flex-direction: column;
}

.separator {
  height: 2px;
  background: whitesmoke;
  border-radius: 50px;
  margin-top: -20px;
}

.nav-logo {
  max-height: 65px;
  display: block;
  margin-left: 40px;
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

.nav-bar-scrolled {
  position: fixed;
  width: 100%;
  left: 50%;
  top: 0;
  transform: translateX(-50%);
  border-radius: 1px;
  height: 145px; /* Increased height when scrolled */
  transition: height 0.3s ease-in-out; /* Smooth transition */
  border-bottom: 1px solid #e5e7eb; /* Add a light gray divider line */
}


.nav-bar-scrolled .searchbox {
  margin-top: 25px;
  width: 70%;
  margin-right: 380px;
}


.search-input {
  padding: 0.75rem 1rem;
  border: 1px solid #9CA3AF;
  border-radius: 0.5rem;
  width: 100%;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: indigo;
}

.search-icon {
  position: absolute;
  top: 50%;
  right: 1rem;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.icon-search {
  width: 1.5rem;
  height: 1.5rem;
  color: #695CFE;
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
</style>
