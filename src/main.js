import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueCookie from 'vue-cookie'

import ListSpaces from './Spaces.vue'
import ListGeneral from './General.vue'
import ListAreas from './Areas.vue'
import Registration from './Registration.vue'
import Workplace from './Workplace.vue'
import TimeSorting from './TimeSorting.vue'
import MembersSorting from './MembersSorting.vue'
import Login from "./Login.vue"
import Main from "./Main.vue"
//------------------------------------------------------
import ToDay from "./ToDay.vue"
import WorkplaceForToday from './WorkplaceForToday.vue'
import TimeSortingForToday from './TimeSortingForToday.vue'
//-------------------------------------------------------

Vue.use( VueRouter )
Vue.use( VueCookie )

Vue.component( 'ListSpaces' 	, ListSpaces )
Vue.component( 'ListGeneral' 	, ListGeneral )
Vue.component( 'ListAreas' 		, ListAreas )
Vue.component( 'Registration' 	, Registration )
Vue.component( 'Workplace'		, Workplace )
Vue.component( 'TimeSorting'	, TimeSorting )
Vue.component( 'MembersSorting'	, MembersSorting )
Vue.component( 'Login'			, Login )
//-------------------------------------------------------
Vue.component( 'ToDay'			, ToDay )
Vue.component( 'TimeSortingForToday'	, TimeSortingForToday )
Vue.component( 'WorkplaceForToday'			, WorkplaceForToday )
//----------------------------------------------------------

var router = new VueRouter({
	routes : [
	{ name : 'login' 		, path: '/login',component : Login },
	{ name : 'registration' , path: '/registration',component : Registration },
	{ name : 'main' 		, path: '/main',component : Main },
//---------------------------------------------------------------------------------
	{ path: '/today',component : ToDay }]
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
})


