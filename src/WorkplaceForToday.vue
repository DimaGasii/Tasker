<template>
	<div class="work_place">
		<div class="title">
			<div class="name-project text"> Сегодня </div>
			
			<div class="sort text" v-bind:class="{ 'sort-focus ' : choiceSort == 0 }" v-on:click="changeChoice(0)"> </div>
			<hr noshade color="#1F6A94">
		</div>
		<time-sorting-for-today v-bind:data="data" v-if="choiceSort == 0"> </time-sorting-for-today>
		
	</div>
</template>

<script>
	export default {
		props : ['data'],
        data () {
            return {
                choiceSort: 0,
                data : [
                {
                	name: "The Beggining",
                	space: "Relocus Tasker",
                	areas: "Design",
	                members: [
	                {
	                	name : "Andrey",
	                	nickname : "Hosstell",
	                	avatar : "./src/img/ava_1.jpg"
	                },
	                {
	                	name : "Sergey",
	                	nickname : "Pro21",
	                	avatar : "./src//img/ava_2.jpg"
	                },
	                {
	                	name : "Pavel",
	                	nickname : "SuperNickname",
	                	avatar : "./src/img/ava_3.jpg"
	                }
	                ],
	                date : "28 марта",
	                description: "Сбор по поводу проекта в кабинете 2-12 в 12:00",
	                subtasks : [
	                	"Обсудить возможный внутрейнний проект",
	                	"Прототип",
	                	"Детальный экран главной",
	                ],
	                tag : "Meeting"
            	}]
            }
        },
        methods : {
        	changeChoice(index) {
        		this.choiceSort = index
        	}
        },
        
    }
</script>

<style>
@font-face 
{
    font-family: 'Roboto', sans-serif;
    src: url(https://fonts.googleapis.com/css?family=Roboto);
}

body
{
	background-color: #F5F5F5;
}

.work_place
{
	background-color: #F5F5F5;
	width: 100%;
	height: 100%;
	
}

.title
{
	padding-top: 10px;
	padding-bottom: 10px;
}	

.name-project 
{
	display: inline-block;
	position: relative;
	left: 20px;
	font-size: 18pt;
}

.text 
{
    font-family: 'Roboto', sans-serif;
    cursor: default;
}

.sort 
{
	display: inline-block;
	position: relative;
	float: right;
	padding-right: 20px;
	font-size: 14pt;
	color: #999999;
}

.sort-focus 
{
	color: #1A587A;
}



.btn
{
	background: #2D9CDB;
	border: 1px solid white;
	border-radius: 5px;
	display: block;
	margin-top: 5px;
	margin-left: auto;
	margin-right: auto;
	width: 210px;
	height: 40px;
	padding: 5px 20px;
	font-family: 'Roboto', sans-serif;
    font-size: 12pt;
    color: white;
    transition: 0.1s;
}

.btn:hover
{
	background: #F5F5F5;
	border: 1px solid #2D9CDB;
	color: #2D9CDB;
	transition: 0.1s;
}

hr /* Синия линия */
{
    position: absolute;
    left: 20px;
    right: 20px;
    margin-top : 5px;
}
</style>