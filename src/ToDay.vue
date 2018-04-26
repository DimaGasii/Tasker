<template>
	<div class="main">
		<div class="bar">
			<list-spaces class="spaces" v-bind:spaces="spaces" v-on:choice='changeSpace' v-on:reload="loadSpaces"></list-spaces>
			<div class="exit">
				<img src="./icon/Exit.svg">
			</div>	
			<div class="exit">
				<img src="./icon/Nut.svg">
			</div>	
		</div>

		<div class="left">
	        <list-general v-bind:counts='general'></list-general>
	        <list-areas v-bind:areas='areas'></list-areas>
		</div>

		<div class="right">
			<workplace-for-today v-bind:data='tasks'></workplace-for-today>
		</div>
	</div>
</template>

<script>
import axios from "axios"

export default {
    data () {
        return {
        	spaces : [ ],
           	general : [ ], 
           	areas : [ ],
           	tasks : [ ],
           	id_space : 0,
           	id_project : 0 
        }
    },
    methods : {
    	changeSpace(id_space){
    		console.log("Зугрузка")
			if ( id_space !== -1 ){
				this.loadAreas(id_space)	
			}
			else {
				this.areas = [ ]
			}
    	},
    	loadAreas(id_space){
    		self = this 
    		console.log("Обновление Areas")
    		if ( id_space !== -1 ){
	    		axios.post("http://localhost:5000/area", {
	    			cookie : this.$cookie.get('cookie'), 
	    			id_space : id_space 
				}).then(function(argument) {
				console.log(argument.data)
					self.general = argument.data['general']
					self.areas = argument.data['areas']
					self.id_space = id_space
				})	
    		}
    		else{
    			self.areas = []
    		}
			
    	},
    	loadTasks(id_project){
    		self = this
    		axios.post("http://localhost:5000/tasks", {
    			cookie : this.$cookie.get('cookie'), 
    			id_project : id_project 
    		}).then(function(argument) {
    			self.tasks = argument.data['tasks']
				
    		})
    	},
    	loadSpaces(){
    		console.log("Обновление Spaces")
    		self = this
			axios.post("http://localhost:5000/space", {
				cookie : this.$cookie.get('cookie')
			}).then(function (argument) {
				self.spaces = argument.data['spaces']
			}).catch(function (error){
				console.log(error)
			})
    	}
    },
    created : function(){
		this.loadSpaces()
		this.loadAreas(this.id_space)
		this.loadTasks(this.id_project)
    }
}	
</script>

<style>
.main
{

}

.bar
{
	position: fixed;
	top: 0px;
	width: 100%;
	height: 50px;
	background-color: #2D9CDB;
	z-index: 10;
}

.left
{
	width: 250px;
	height: 100%;
}

.right
{
	position: relative;
	left: 250px;
	width: calc(100% - 250px);
	top:-57px;
}

.exit 
{
	position: relative;
	float: right;
	padding: 11px 10px 5px 12px;
	z-index: 100;
	fill: red;
}

.exit:hover 
{
	background-color: #F5F5F5;
}



</style>