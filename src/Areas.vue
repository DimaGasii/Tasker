<template>
	<div class="areas">
		<div class="area" v-for="area in areas"> 
			<div class="title"> {{ area.title }} </div>
			<div class="list">
				<div class="option" v-for="project in area.projects">
					<img class="icon" v-bind:src="project.icon">
					<div class="text"> {{ project.name }} </div>
				</div>
				<div class="empty"> </div>
			</div>
		</div>

		<div class="adding">
			<!-- <button class="btn"> New area </button>
			<button class="btn"> New project </button> -->
            <div class="option-btn">
                <div class="center"> New Area </div> 
            </div>
            <div class="option-btn"> 
                <div class="center"> New project </div> 
            </div>
		</div>
	</div>
</template>

<script>
	export default {
        props : ["areas"],
        data () {
            return {
                
            }
        }
    }
</script>

<style scoped>
@font-face 
{
    font-family: 'Roboto', sans-serif;
    src: url(https://fonts.googleapis.com/css?family=Roboto);
}

.areas
{
	position: absolute;
	top: 158px;
	width: 250px;
	bottom: 0px;
	background-color: #F5F5F5;
}

.area
{
	position: relative;
}

.title
{
	position: relative;
	color : #2D9CDB;
	font-size: 12pt;
	font-family: 'Roboto', sans-serif;
	left: 15px;
	top: 5px;
    padding: 0px;
}

.list 
{
	margin-top: 10px;
}

.text /*Текст внутри ячейки */
{
    position: relative;
    float: left;
    left : 30px;
    top: 3px;
    text-align: center;
    font-family: 'Roboto', sans-serif;
    cursor: default;
    font-size: 10pt;
}


.icon /* Иконка внутри ячейки */
{
    position: relative;
    float: left;
    left : 15px;
    width: 20px;
    height: 20px;
}

.option /* Ячейка с текстом и иконкой */ 
{
    height: 20px;
    padding: 3px 0px;
    color: #333333;
}


.option:hover 
{
	background-color: #999999;
	color: white;
}

.adding
{
	position: fixed;
	background-color: #2D9CDB;
	height: 100px;
	width: 250px;
	bottom: 0px;
    border-radius: 0px;
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
	width: 225px;
	height: 40px;
	padding: 5px 20px;
	font-family: 'Roboto', sans-serif;
    font-size: 12pt;
    color: white;
}

.btn:hover
{
	background: #F5F5F5;
	border: 1px solid #2D9CDB;
	color: #2D9CDB;
	transition: 0.2s;
}

.option-btn /*Ячейка со спейсом и иконкой*/ 
{

    transition: 0.5s;
    background-color: #2D9CDB;
    color: white;
    width: 250px;
    height: 50px;
    /*transition : 0.2s;*/
    
}

.option-btn:hover /*Ячейка со спейсом и иконкой*/ 
{
    transition: 0.5s;
    background-color: white;
    width: 250px;
    height: 50px;
    transition : 0.2s;
    color: #2D9CDB;
    /*border: 1px solid #2D9CDB;*/
}

.center
{
    position: relative;
    font-family: 'Roboto', sans-serif;
    cursor: default;
    font-size: 11pt;
    text-align: center;
    top: 17px;
}

.empty
{
	height: 10px;
}



</style>