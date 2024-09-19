<template>
  <div>
    <div class="search-box-wrapper z-1">
      <div class="search-box-container">
        <h2 class="search-title">Search for residences</h2>

        <div class="search-controls flex items-center">
          <!-- Search Input -->
          <div class="relative flex-grow mb-4">
            <input v-model="searchQuery" type="text" class="search-input" placeholder="Enter your search...">
            <span class="search-icon">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
            </span>
          </div>

          <!-- "Or" Text with Gray Lines -->
          <div class="flex items-center justify-center ml-2 mb-4">
            <div class="line"></div>
            <div class="text-or">or</div>
            <div class="line"></div>
          </div>

          <!-- Location Button -->
          <div class="flex items-center justify-center ml-2 mb-4">
            <button @click="submit" class="location-button">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon-location" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 2a5 5 0 00-5 5c0 3.866 5 10 5 10s5-6.134 5-10a5 5 0 00-5-5zm0 7a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button @click="submit" :disabled="loading" class="submit-button">
          {{ loading ? 'Loading...' : 'Submit Search' }}
        </button>
      </div>
      <h1 hidden class="font-semibold">Showing results for "{{ searchQuery }}"</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isScrolled: false,
      searchQuery: '',
      loading: false,
      showMenu: false
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
    },
    async submit() {
      this.loading = true;
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/accommodations/', {
          params: {
            q: this.searchQuery
          }
        });
        this.$emit('search-results-updated', response.data);
        window.scrollTo({
          top: 470,
          behavior: 'smooth'
        });
      } catch (error) {
        console.error('Error fetching search results:', error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
@import 'https://fonts.googleapis.com/css?family=Mada:400,500';

.search-box-wrapper {
  margin-top: -250px;
}

.search-box-container {
  background-color: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  max-width: 600px;
  height: auto;
  margin: 0 auto;
  margin-top: 2rem;
}

.search-title {
  font-size: 1.5rem;
  color: #4B5563;
  margin-bottom: 1rem;
  text-align: center;
}

.search-controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.location-button {
  background-color: white;
  border: 1px solid #E5E7EB;
  border-radius: 0.5rem;
  padding: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.location-button:hover {
  background-color: #F3F4F6;
}

.icon-location {
  width: 1.5rem;
  height: 1.5rem;
  color: #6366F1;
}

.line {
  border-top: 1px solid #D1D5DB;
  width: 25%;
}

.text-or {
  margin: 0 1rem;
  color: #9CA3AF;
}

.search-input {
  padding: 0.75rem 1rem;
  border: 1px solid #E5E7EB;
  border-radius: 0.5rem;
  width: 100%;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #9CA3AF;
}

.search-icon {
  position: absolute;
  top: 50%;
  right: 1rem;
  transform: translateY(-50%);
  pointer-events: none;
}

.icon-search {
  width: 1.5rem;
  height: 1.5rem;
  color: #9CA3AF;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
}

.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.submit-button {
  background-color: #4B5563;
  color: white;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 100%;
  text-align: center;
  margin-top: 1rem;
}

.submit-button:hover {
  background-color: #2D3748;
}

.submit-button:disabled {
  background-color: #9CA3AF;
  cursor: not-allowed;
}

@media (max-width: 640px) {
  .search-box-wrapper {
    margin-top: -50px;
  }

  .search-box-container {
    padding: 1.5rem;
    max-width: 100%;
  }

  .search-title {
    font-size: 1.25rem;
  }

  .search-controls {
    flex-direction: column;
  }

  .location-button, .text-or, .line {
    margin-top: 1rem;
    width: 100%;
  }
}
</style>
