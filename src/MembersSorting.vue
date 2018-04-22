<template>
	<div class="members-sorting">
		<div class="user" v-for="member in formatForMembersSorting">
			<div class="member">
				<div class="avatar"> 
					<img v-bind:src="member.avatar">
				</div> 
				<div class="name"> {{ member.name }} {{ member.nickname }} </div>
			</div>

			<div class="title" v-on:click='changeChoice' v-for="task in member.tasks">
				<div class="name-task"> 
					{{ task.name }}
					<div class="circle"></div> 
					<div class="tag"> {{ task.tag }} </div> 
				</div> 
				<div class="members"> 
					<div class="ava" v-for="user in task.members"> 
						<img v-bind:src="user.avatar">
					</div> 

					<div class="line"> </div>
					<div class="date"> {{ task.date}}  </div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
        props : ["data"],
        computed : {
        	formatForMembersSorting(){
        		var nicknames = [ ]
        		var mas = [ ]
        		var index = 0 
        		this.data.forEach( function ( item ) {
        			item.members.forEach( function ( member )
        			{
        				if ( nicknames.indexOf(member.nickname) != -1 )
        				{
        					index = nicknames.indexOf(member.nickname)
        					mas[index].tasks.push(item)
        				}
        				else 
        				{
        					nicknames.push(member.nickname)
        					mas.push({
        						name : member.name,
        						nickname : member.nickname,
        						avatar : member.avatar,
        						tasks : [ item ]
        					})
        				}
        				
        			})
        		})
        		console.log(mas)
        		return mas
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

.members-sorting
{
	position: relative;	
	padding-left: 20px;
	padding-bottom: 30px;
	padding-top: 10px;
	background-color: #F5F5F5;
	height: 100%;
}

.user 
{
	padding-bottom: 25px;
}

.member
{
	display: inline-block;
	width: 100%;
	padding-bottom: 10px;
}

.title
{
	display: inline-block;
	width: 100%;
	padding-top: 1px;
}

.name-task
{
	display: inline-block;
	color: #1A587A;
	
	font-family: 'Roboto', sans-serif;
	font-size: 14pt;
}

.name
{
	position: relative;
	display: inline-block;
	color: #1A587A;
	top: -13px;
	font-family: 'Roboto', sans-serif;
	font-size: 14pt;
	padding-left: 12px;
}

.avatar 
{

	border: 3px solid white;
	position: relative;
	display: inline-block;
	width: 35px;
	height: 35px;
	border-radius: 40px;
	overflow: hidden;
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

.tag 
{
	position: relative;
	display: inline-block;
	color: #999999;
	font-size: 13pt;
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
	/*margin-left: 2%;
	margin-right: 2%;*/
}


.date
{
	position: relative;
	display: inline-block;
	color: #999999;
	font-family: 'Roboto', sans-serif;
	top: -12px;
	font-size: 12pt;
}

img
{
	height: 50px;
}

</style>