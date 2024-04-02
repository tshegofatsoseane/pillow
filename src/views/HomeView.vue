<template>
  <div class="home">
  <HomeNavBar />
  <Hero />
 
  <Searchbox @search-submitted="showResults = true" />

  <SearchResults v-if="showResults" />
  <SearchResults v-if="showResults" />
  <SearchResults v-if="showResults" />

 <FeaturedResidancesMaf />
 <FeaturedResidancesPotch/>
 <FeaturedResidancesVaal/>

  </div>
  
</template>

<script>
import Hero from '@/components/Hero.vue'
import FeaturedResidancesMaf from '@/components/FeaturedResidancesMaf.vue'
import FeaturedResidancesPotch from '@/components/FeaturedResidancesPotch.vue'
import FeaturedResidancesVaal from '@/components/FeaturedResidancesVaal.vue'
import SearchResults from '@/components/SearchResults.vue'
import Searchbox from '@/components/Searchbox.vue'
import HomeNavBar from '@/components/HomeNavBar.vue'

export default {
  name: 'HomeView',
  components: {
    HomeNavBar, Hero, FeaturedResidancesMaf, Searchbox, FeaturedResidancesPotch, FeaturedResidancesVaal, SearchResults
  },
  data() {
    return {
      showResults: false
    }
  }
}
</script>
