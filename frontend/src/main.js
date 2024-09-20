import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/main.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

// Import Font Awesome core and icon components
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';


// Import specific icons
import { faSchool, faBuilding, faBed, faBuildingColumns, faHouse, faTree, faBicycle, faStore, faWifi, faLock } from '@fortawesome/free-solid-svg-icons';

// Add icons to the library
library.add(faSchool, faBuilding, faBed, faBuildingColumns, faHouse, faTree, faBicycle, faStore, faWifi, faLock);

// Create and mount the Vue application
const app = createApp(App);
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon);
app.mount('#app');
