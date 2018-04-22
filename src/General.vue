<template>
	<div class="general">
        
		<div class="option">
			<img class="icon" src="./icon/Today.svg">
			<div class="text"> Today </div>
			<div class="count"> {{ counts[0] }} </div>
		</div>
		<div class="option">
			<img class="icon" src="./icon/Next.svg">
			<div class="text"> Upcoming  </div>
			<div class="count"> {{ counts[1] }} </div>
		</div>
		<div class="option">
			<img class="icon" src="./icon/Logbook.svg">
			<div class="text"> Logbook </div>
		</div>
		<div class="option">
			<img class="icon" src="./icon/Overdue.svg">
			<div class="text"> Overdue </div>
			<div class="count"> {{ counts[2] }} </div>
		</div>
		<hr noshade color="#2D9CDB">
        <div class="v-line"></div>
	</div>
</template>

<script>
	export default {
        props : ['counts'],
        data () {
            return {
                
            }
        },
        method: {
            some() {
                console.log(counts)
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

.general
{	
	top:52px;
	position: relative;
	width: 250px;
	background-color: #F5F5F5;
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

.icon /* Иконка внутри ячейки */
{
    position: relative;
    float: left;
    left : 15px;
    top: 0px;
    width: 20px;
    height: 20px;
}

.text /*Текст внутри ячейки */
{
    position: relative;
    float: left;
    left : 30px;
    top: 3px;
    text-align: center;
    font-family: 'Roboto', sans-serif;
    font-size: 10pt;
    cursor: default;
}

.count
{
	position: relative;
    float: right;
    right: 20px;
    top: 3px;
    text-align: center;
    font-family: 'Roboto', sans-serif;
    font-size: 10pt;
    cursor: default;
}

.v-line
{
    position: absolute;
    background: #2D9CDB;;
    top: 0px;
    width: 2px;
    height: 600px;
    float: right;
    right:-2px;
    z-index: 100;
}

hr /* Белая линия */
{
    position: relative;
    width: 238px;
    margin : 0px;
    left : 5px;
}
</style>