import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ExploreView from '../views/ExploreView.vue'
import InnovationView from '../views/InnovationView.vue'
import APIView from '../views/APIView.vue'
import TechnologyView from '../views/TechnologyView.vue'
import SignupView from '../views/SignupView.vue'
import ResultDetailsView from '../views/ResultDetailsView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/explore',
    name: 'explore',
    component: ExploreView
  },
  {
    path: '/innovation',
    name: 'innovation',
    component: InnovationView
  },
  {
    path: '/api',
    name: 'api',
    component: APIView
  },
  {
    path: '/technology',
    name: 'technology',
    component: TechnologyView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/details/:id', // Include route parameter for details view
    name: 'details',
    component: ResultDetailsView,
    props: true // Pass route params as props to the component
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
