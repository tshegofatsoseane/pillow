<template>
  <div>
    <h1 class="text-4xl font-semibold text-gray-500 mt-16">
      Popular Universities in South Africa
    </h1>

    <div class="tabs mt-8">
      <ul class="tab-list mt-8">
        <li
          v-for="tab in tabs"
          :key="tab.id"
          :class="{ 'active-tab': activeTab === tab.id }"
          @click.prevent="activeTab = tab.id"
          class="tab"
        >
          <a class="tab-link">{{ tab.label }}</a>
        </li>
      </ul>
      <div class="separator my-8"></div>

      <div style="margin-top: 120px;" v-if="activeTab === 'all'" class="tab-content">
        <FeaturedAccommodations university="NWU" campus="" />
        <FeaturedAccommodations university="UJ" campus="" />
        <FeaturedAccommodations university="UFS" campus="" />
        <FeaturedAccommodations university="WITS" campus="" />
        />
      </div>

      <div style="margin-top: 120px;" v-if="activeTab === 'nwu'" class="tab-content">
        <FeaturedAccommodations university="NWU" campus="Mahikeng" />
        <FeaturedAccommodations university="NWU" campus="Potchefstroom" />
        <FeaturedAccommodations university="NWU" campus="Vanderbijlpark" />
      </div>

      <div style="margin-top: 120px;" v-if="activeTab === 'uj'" class="tab-content">
        <FeaturedAccommodations university="UJ" campus="Doornfontein Campus" />
        <FeaturedAccommodations university="UJ" campus="Soweto Campus" />
      </div>

      <div style="margin-top: 120px;" v-if="activeTab === 'ufs'" class="tab-content">
        <FeaturedAccommodations university="UFS" />
      </div>

      <div style="margin-top: 120px;" v-if="activeTab === 'wits'" class="tab-content">
        <FeaturedAccommodations university="WITS" />
      </div>
    </div>
  </div>
</template>

<script>
import FeaturedAccommodations from '@/components/FeaturedAccommodations.vue';

export default {
  name: 'AccommodationTabs',
  components: {
    FeaturedAccommodations,
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
      universities: ['NWU', 'UJ', 'WITS', 'UFS'],
      accommodations: [], // Store combined accommodations here
    };
  },
  methods: {
    async fetchAllAccommodations() {
      const promises = this.universities.map((uni) =>
        fetch(`http://127.0.0.1:8000/api/accommodations/?university=${uni}`).then(res => res.json())
      );
      const results = await Promise.all(promises);
      this.accommodations = results.flatMap(data => data.results);
    },
    filterAccommodations(university, campus = '') {
      return this.accommodations.filter(
        accommodation =>
          accommodation.university === university &&
          (!campus || accommodation.nearest_campus === campus)
      );
    },
  },
  created() {
    this.fetchAllAccommodations();
  },
};
</script>

<style scoped>
.separator {
  height: 2px;
  background: whitesmoke;
  border-radius: 20px;
  width: 1450px;
}
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
