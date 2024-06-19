<template>
  <div>
  <nav
    id="nav-bar"
    :class="['nav', isScrolled ? 'nav-bar-scrolled' : 'nav-bar-top']"
    @scroll="handleScroll"
   >
    <div class="wrapper flex justify-between items-center z-50">
            <!-- Logo -->
  <div class="flex items-center ml-6">
  <img src="@/assets/logo.png" alt="Pillow Logo" class="h-8 w-auto mr-2">
  <div class="text-2xl font-bold border-white rounded-full " :class="{ 'text-indigo-500': isScrolled }">Pillow</div>
</div>
      <input type="checkbox" id="menu-toggle" class="hidden">
      <label for="menu-toggle" class="label-toggle hamburger"></label>

      <ul class="menu-list flex justify-around items-center">
            <!-- Navigation Links -->
            <div :class="{ 'hidden': !showMenu, 'lg:flex': showMenu }" class="lg:flex hover:border-white">
                <router-link to="/" class=" font-semibold px-4 py-4 transition duration-700 ease-in-out hover:text-indigo-700 hover:border-blue-500" :class="{ 'border-b-2 border-blue-500': $route.path === '/', 'text-black border-indigo-500': isScrolled }">Home</router-link>
                <router-link :to="{ name: 'innovation' }" class=" font-semibold px-4 py-4 transition duration-300 ease-in-out hover:text-indigo-700 hover:border-blue-500" :class="{ 'border-b-2 border-blue-500': $route.name === 'innovation', 'text-black border-indigo-400': isScrolled }">For Landlords</router-link>
            </div>

      </ul>

      <!-- Action Buttons -->
<div class="mr-12 flex items-center space-x-4"> 
    <router-link :to="{ name: 'innovation' }" class="border font-semibold py-2 px-6 rounded transition duration-300 ease-in-out hover:text-indigo-500 hover:border-indigo-900">Login</router-link>
<router-link :to="{ name: 'signup' }"  class="bg-gradient-to-r from-indigo-600/90 to-pink-800/50 hover:bg-indigo-600/60 text-white font-semibold py-2 px-6 rounded transition duration-300 ease-in-out">Signup</router-link>
</div>
  
    </div>
  </nav>
 
</div>
</template>

<script>
export default {
  data() {
    return {
      isScrolled: false
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
    }
  }
};
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css?family=Mada:400,500';



.nav {
  height: 85px;
  transition: width 0.2s ease-in-out;
  margin-top: -15px;
  background-color: #fff;
  border-radius: 30px;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.1);
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

  .menu-list {
    background-color: #fff;
    width: 100%;
    margin: 90px auto 0;
    display: block;
    height: 0;
    list-style-type: none;
    opacity: 0;
    padding: 0;
    text-align: center;
    visibility: hidden;
  }
  .menu-list li {
    border-top: 2px solid #e0696c;
    color: #000;
    display: block;
    max-width: 100%;
    font-size: 1.2em;
    padding: 1em 0;
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

  .hamburger {
    background: linear-gradient(
      to bottom,
      #e0696c 0%,
      #e0696c 20%,
      transparent 20%,
      transparent 40%,
      #e0696c 40%,
      #e0696c 60%,
      transparent 60%,
      transparent 80%,
      #e0696c 80%,
      #e0696c 100%
    );
  }
}
</style>
