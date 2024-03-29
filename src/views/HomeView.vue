<template>
  <div class="home">
  <Hero />
  <Searchbox />

<SearchResults />
<SearchResults />
<SearchResults />



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

export default {
  name: 'HomeView',
  components: {
      Hero, FeaturedResidancesMaf, Searchbox, FeaturedResidancesPotch, FeaturedResidancesVaal, SearchResults
  }
}
</script>
