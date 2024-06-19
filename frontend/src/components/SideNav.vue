<template>
    <div id="app" :class="{ dark: isDarkMode }">
      <!-- Top Navigation Bar -->
      <nav class="top-nav">
        <div class="user-info">
          <img src="@/assets/logo.png" alt="User Profile" class="profile-pic">
          <span class="username">John Doe</span>
        </div>
        <div class="nav-actions">
          <a href="#" @click="logout" class="logout">Logout</a>
        </div>
      </nav>
      
      <!-- Sidebar Navigation -->
      <nav class="sidebar" :class="{ close: isSidebarClosed }">
        <header>
          <div class="image-text">
            <span class="image">
              <img src="@/assets/logo.png" alt="Logo">
            </span>
            <div class="text logo-text">
              <span class="name">Pillow.com</span>
              <span class="profession">Landlord Dashboard</span>
            </div>
          </div>
          <i class='bx bx-chevron-right toggle' @click="toggleSidebar"></i>
        </header>
        <div class="menu-bar">
          <div class="menu">
            <li class="search-box">
              <i class='bx bx-search icon'></i>
              <input type="text" placeholder="Search..." @focus="openSidebar">
            </li>
            <ul class="menu-links">
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-home-alt icon'></i>
                  <span class="text nav-text">Dashboard</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-bar-chart-alt-2 icon'></i>
                  <span class="text nav-text">Revenue</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-bell icon'></i>
                  <span class="text nav-text">Notifications</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-pie-chart-alt icon'></i>
                  <span class="text nav-text">Analytics</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-heart icon'></i>
                  <span class="text nav-text">Likes</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-wallet icon'></i>
                  <span class="text nav-text">Wallets</span>
                </a>
              </li>
            </ul>
          </div>
          <div class="bottom-content">
            <li>
              <a href="#">
                <i class='bx bx-log-out icon'></i>
                <span class="text nav-text">Logout</span>
              </a>
            </li>
            <li class="mode">
              <div class="sun-moon">
                <i class='bx bx-moon icon moon'></i>
                <i class='bx bx-sun icon sun'></i>
              </div>
              <span class="mode-text text">{{ modeText }}</span>
              <div class="toggle-switch" @click="toggleDarkMode">
                <span class="switch"></span>
              </div>
            </li>
          </div>
        </div>
      </nav>
  
      <section class="home">
        <div class="text"></div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isSidebarClosed: true,
        isDarkMode: false,
      };
    },
    computed: {
      modeText() {
        return this.isDarkMode ? "Light mode" : "Dark mode";
      },
    },
    methods: {
      toggleSidebar() {
        this.isSidebarClosed = !this.isSidebarClosed;
      },
      openSidebar() {
        this.isSidebarClosed = false;
      },
      toggleDarkMode() {
        this.isDarkMode = !this.isDarkMode;
      },
      logout() {
        // Handle logout logic here
        console.log("Logging out...");
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  @import url('https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css');
  
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
  }
  
  body {
    min-height: 100vh;
    background-color: white;
    transition: all 0.5s ease;
  }
  
  ::selection {
    background-color: #695CFE;
    color: #fff;
  }
  
  body.dark {
    background-color: #18191a;
  }
  
  /* Top Navigation Bar */
  .top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #FFF;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .top-nav .user-info {
    display: flex;
    align-items: center;
  }
  
  .top-nav .user-info .profile-pic {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }
  
  .top-nav .user-info .username {
    font-size: 16px;
    font-weight: 500;
  }
  
  .top-nav .nav-actions .logout {
    color: #695CFE;
    text-decoration: none;
    font-size: 16px;
  }
  
  body.dark .top-nav {
    background-color: #242526;
  }
  
  body.dark .top-nav .nav-actions .logout {
    color: #ccc;
  }
  
  .sidebar {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 250px;
    padding: 10px 14px;
    background: #FFF;
    transition: all 0.5s ease;
    z-index: 100;
    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.1);
  }
  
  .sidebar.close {
    width: 88px;
  }
  
  .sidebar li {
    height: 50px;
    list-style: none;
    display: flex;
    align-items: center;
    margin-top: 10px;
  }
  
  .sidebar header .image,
  .sidebar .icon {
    min-width: 60px;
    border-radius: 6px;
  }
  
  .sidebar .icon {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
  
  .sidebar .text,
  .sidebar .icon {
    color: #707070;
    transition: all 0.3s ease;
  }
  
  .sidebar .text {
    font-size: 17px;
    font-weight: 500;
    white-space: nowrap;
    opacity: 1;
  }
  
  .sidebar.close .text {
    opacity: 0;
  }
  
  .sidebar header {
    position: relative;
  }
  
  .sidebar header .image-text {
    display: flex;
    align-items: center;
  }
  
  .sidebar header .logo-text {
    display: flex;
    flex-direction: column;
  }
  
  header .image-text .name {
    margin-top: 2px;
    font-size: 18px;
    font-weight: 600;
  }
  
  header .image-text .profession {
    font-size: 16px;
    margin-top: -2px;
    display: block;
  }
  
  .sidebar header .image {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .sidebar header .image img {
    width: 40px;
    border-radius: 6px;
  }
  
  .sidebar header .toggle {
    position: absolute;
    top: 50%;
    right: -25px;
    transform: translateY(-50%) rotate(180deg);
    height: 25px;
    width: 25px;
    background-color: #695CFE;
    color: #FFF;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    cursor: pointer;
    transition: all 0.5s ease;
  }
  
  body.dark .sidebar header .toggle {
    color: #ccc;
  }
  
  .sidebar.close .toggle {
    transform: translateY(-50%) rotate(0deg);
  }
  
  .sidebar .menu {
    margin-top: 40px;
  }
  
  .sidebar li.search-box {
    border-radius: 6px;
    background-color: #F6F5FF;
    cursor: pointer;
    transition: all 0.5s ease;
  }
  
  .sidebar li.search-box input {
    height: 100%;
    width: 100%;
    outline: none;
    border: none;
    background-color: #F6F5FF;
    color: #707070;
    border-radius: 6px;
    font-size: 17px;
    font-weight: 500;
    transition: all 0.5s ease;
  }
  
  .sidebar li a {
    list-style: none;
    height: 100%;
    background-color: transparent;
    display: flex;
    align-items: center;
    height: 100%;
    width: 100%;
    border-radius: 6px;
    text-decoration: none;
    transition: all 0.3s ease;
  }
  
  .sidebar li a:hover {
    background-color: #695CFE;
  }
  
  .sidebar li a:hover .icon,
  .sidebar li a:hover .text {
    color: white;
  }
  
  body.dark .sidebar li a:hover .icon,
  body.dark .sidebar li a:hover .text {
    color: #ccc;
  }
  
  .sidebar .menu-bar {
    height: calc(100% - 55px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow-y: auto;
  }
  
  .menu-bar::-webkit-scrollbar {
    display: none;
  }
  
  .menu-bar .mode {
    border-radius: 6px;
    background-color: #F6F5FF;
    position: relative;
    transition: all 0.5s ease;
  }
  
  .menu-bar .mode .sun-moon {
    height: 50px;
    width: 60px;
  }
  
  .sun-moon i {
    position: absolute;
    height: 100%;
    width: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 19px;
  }
  
  .mode-text {
    font-size: 16px;
    font-weight: 500;
    color: #707070;
  }
  
  .toggle-switch {
    position: absolute;
    right: 0;
    height: 100%;
    min-width: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 6px;
    cursor: pointer;
  }
  
  .toggle-switch .switch {
    position: relative;
    height: 22px;
    width: 40px;
    border-radius: 25px;
    background-color: #DDD;
    transition: all 0.5s ease;
  }
  
  .switch::before {
    content: '';
    position: absolute;
    height: 15px;
    width: 15px;
    border-radius: 50%;
    top: 50%;
    left: 5px;
    transform: translateY(-50%);
    background-color: #FFF;
    transition: all 0.4s ease;
  }
  
  body.dark .switch::before {
    left: 20px;
  }
  
  .home {
    position: absolute;
    top: 0;
    left: 250px;
    height: 100vh;
    width: calc(100% - 250px);
    background-color: whitesmoke;
    transition: all 0.5s ease;
  }
  
  .home .text {
    font-size: 30px;
    font-weight: 500;
    color: #707070;
    padding: 12px 60px;
  }
  
  .sidebar.close ~ .home {
    left: 78px;
    height: 100vh;
    width: calc(100% - 78px);
  }
  
  body.dark .home .text {
    color: #ccc;
  }
  </style>
  