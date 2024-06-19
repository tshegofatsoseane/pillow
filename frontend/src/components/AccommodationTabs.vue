<template>
    
<div>

    <h1 class="text-4xl font-semibold text-gray-500  mt-16">
           Popular Universities in South Africa
    </h1>



    <div class="tabs mt-8">
      <ul class="tab-list  mt-8">
        <li
          v-for="tab in tabs"
          :key="tab.id"
          :class="{ 'active-tab': activeTab === tab.id }"
          @click="activeTab = tab.id"
          class="tab"
        >
          <a href="#" class="tab-link">{{ tab.label }}</a>
        </li>
      </ul>
      <!-- Decorative line separator -->
      <div class="separator my-8"></div>
  
      <div v-if="activeTab === 'all'" class="tab-content">
        <NWUResidances />
        <UJResidances />
      </div>
      <div v-if="activeTab === 'nwu'" class="tab-content">
        <!-- Display NWU related accommodations -->
        <FeaturedResidancesMaf
          :accommodations="fetchedAccommodations.results.filter(accommodation => accommodation.university === 'NWU')"
        />
        <FeaturedResidancesPotch />
        <FeaturedResidancesVaal />
      </div>
      <div v-if="activeTab === 'uj'" class="tab-content">
        <!-- Display UJ related accommodations -->
        <UJResidances
          :accommodations="fetchedAccommodations.results.filter(accommodation => accommodation.university === 'UJ')"
        />
      </div>
      <div v-if="activeTab === 'ufs'" class="tab-content">
        <!-- Display UFS related accommodations -->
      </div>
      <div v-if="activeTab === 'wits'" class="tab-content">
        <!-- Display WITS related accommodations -->
      </div>
    </div>
</div>
  </template>
  
  <script>
  import FeaturedResidancesMaf from '@/components/FeaturedResidancesMaf.vue'
  import FeaturedResidancesPotch from '@/components/FeaturedResidancesPotch.vue'
  import FeaturedResidancesVaal from '@/components/FeaturedResidancesVaal.vue'
  import UJResidances from '@/components/UJResidances.vue'
  import NWUResidances from '@/components/NWUResidances.vue'
  
  export default {
    name: 'AccommodationTabs',
    components: {
      NWUResidances,
      UJResidances,
      FeaturedResidancesMaf,
      FeaturedResidancesPotch,
      FeaturedResidancesVaal,
    },
    props: {
      fetchedAccommodations: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        activeTab: 'all',
        tabs: [
          { id: 'all', label: 'All' },
          { id: 'nwu', label: 'NWU' },
          { id: 'uj', label: 'UJ' },
          { id: 'ufs', label: 'UFS' },
          { id: 'wits', label: 'WITS' },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .separator {
    height: 2px;
    background: whitesmoke;
    border-radius: 20px;
    width: 1300px;
    margin-left: 150px;
  }
  
  /* Custom styles for the tabs */
  .tab-list {
    display: flex;
    gap: 16px;
    padding: 10px;
    background-color: #f3f4f6;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 80%;
    max-width: 600px;
    margin: 0 auto;
  }
  
  .tab {
    list-style: none;
    cursor: pointer;
    transition: transform 0.3s ease, background-color 0.3s ease;
  }
  
  .tab-link {
    display: block;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: 500;
    color: #374151;
    text-decoration: none;
    transition: color 0.3s ease, background-color 0.3s ease;
  }
  
  .tab:hover {
    transform: translateY(-3px);
  }
  
  .tab-link:hover {
    background-color: #e5e7eb;
    color: #1f2937;
  }
  
  .active-tab .tab-link {
    background-color: #6366f1;
    color: #ffffff;
  }
  
  @media screen and (max-width: 640px) {
    .tab-link {
      padding: 8px 16px;
      font-size: 14px;
    }
  }
  </style>
  