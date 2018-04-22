<template>
	<div class="time-sorting">
		<div class="task" v-for="d in data">
			<div class="title">
				<div class="name-task"> 
					{{ d.name }} 
					<div class="circle"></div> 
					<div class="tag"> {{ d.tag }} </div> 
				</div> 
				<div class="members"> 
					<div class="ava" v-for="member in d.members"> 
						<img v-bind:src="member.avatar">
					</div> 
					<div class="line"> </div>
					<div class="date"> {{ d.date }} </div>
				</div>
			</div>

			<div class="description"> {{ d.description }} </div>

			<div class="subtasks" v-for="( subtask , index ) in d.subtasks">
				<label>
	                <input class="checkbox" type="checkbox" name="checkbox-test" >
	                <span class="checkbox-custom"></span>
	                <span class="label"> {{ subtask }} </span>
	            </label>
			</div>

			<div class="subtasks">
				<img class="icon" src="./icon/Plus.svg">
				<span class="newsub"> New subtask </span> 
			</div>
		</div>
		

		<button class="new-task btn">
			New Task 
		</button>
	</div>
</template>

<script>
	export default {
		props : ["data"],
        data () {
            return {
  
            }
        },
        methods : {

        }
     }
</script>

<style>
@font-face 
{
    font-family: 'Roboto', sans-serif;
    src: url(https://fonts.googleapis.com/css?family=Roboto);
}

.time-sorting
{
	position: relative;	
	padding-left: 20px;
	padding-bottom: 30px;
	background-color: #F5F5F5;
	height: 100%;

}

.task
{
	padding-bottom: 20px;
}

.title
{
	display: inline-block;
	width: 100%;
	padding-top: 10px;
}

.name-task
{
	display: inline-block;
	color: #1A587A;
	
	font-family: 'Roboto', sans-serif;
	font-size: 14pt;

}

.members
{
	display: inline-block;
	position: relative;
	float: right;
	padding-right: 20px;
	height: 20px;
}

.ava 
{
	border: 2px solid #F5F5F5;
	position: relative;
	display: inline-block;
	width: 25px;
	height: 25px;
	border-radius: 40px;
	overflow: hidden;
	margin-left: -10px;
	top: -3px;
}

.line
{
	position: relative;
	display: inline-block;
	background-color: #999999;
	width: 2px;
	height: 30px;
	top: -3px;
	margin-left: 10px;
	margin-right: 10px;
}

.date
{
	position: relative;
	display: inline-block;
	color: #999999;
	font-family: 'Roboto', sans-serif;
	top: -12px;
	font-size: 13pt;
}

.description
{
	margin-bottom: 1px;
	font-family: 'Roboto', sans-serif;
	font-size: 13pt;
	
}

.subtasks
{
	
	left: 10px;
	padding-top: 7px;
	font-size: 12pt;
}


.checkbox
{
	display: none;
}

.checkbox-custom 
{
	position: relative;   
	width: 15px;             
	height: 15px;        
	border: 1px solid #1A587A;
	border-radius: 6px;
}

.label
{
	margin-left: 10px;
	font-size: 14px;
	font-family: 'Roboto', sans-serif;
}

.checkbox-custom, .label 
{
	display: inline-block;
	vertical-align: middle;
}

.checkbox:checked + .checkbox-custom::before 
{
	content: "";             
	display: block;			 
	position: absolute;      
	top: 3px;
	right: 3px;
	bottom: 3px;
	left: 3px;
	background: #1A587A;
	border-radius: 4px;
}

.icon 
{
    position: relative;
    float: left;
    left: -1px;
    top: -1px;
    width: 20px;
    height: 20px;
}

.newsub
{
	margin-left: 10px;
	font-size: 17px;
	font-family: 'Roboto', sans-serif;
	color: #AAAAAA;
	cursor: default;
}

.newsub:hover
{
	color: #1A587A;
}

.adding
{
	position: absolute;
	background-color: #999999;
	width: 200px;
	height: 200px;
	border-radius: 10px;
}

.circle 
{
	position: relative;
	display: inline-block;
	background-color: #999999;
	border-radius: 10px;
	width: 8px;
	height: 8px;
	margin: 0px 10px ;
	top: -2px;
}

.new-task 
{
	position: fixed;
	right: 10px;
	bottom: 10px;
}

.tag 
{
	position: relative;
	display: inline-block;
	color: #999999;
	font-size: 13pt;
}

img
{
	height: 30px;
}

</style>