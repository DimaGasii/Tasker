<template>
	<div class="registration">
		<div class="left">
			<div class="text sign"> Sign Up</div>
		</div>
		<div class="right">
			<div class="input-div">
				<div class="input-sub-div"> 
					<input type="text" class="input" v-model="name" v-on:input="changeName(0,'name')">
					<div class="text name-input" v-bind:class="{ 'name-up' : filling[0] }"> Name </div>
				</div>
				<div class="input-sub-div"> 
					<input type="text" class="input" v-model="nickname" v-on:input="changeName(1,'nickname')">
					<div class="text name-input" v-bind:class="{ 'name-up' : filling[1] }"> Nickname </div>
				</div>
				<div class="input-sub-div"> 
					<input type="text" class="input" v-model="email" v-on:input="changeName(2,'email')">
					<div class="text name-input" v-bind:class="{ 'name-up' : filling[2] }"> E-mail </div>
				</div>
				<div class="input-sub-div"> 
					<input type="password" class="input" v-model="password" v-on:input="changeName(3,'password')">
					<div class="text name-input" v-bind:class="{ 'name-up' : filling[3] }"> Password </div>
				</div>
			</div>
			<div class="start">
				<button class="btn text"> Get started </button>
				<div class="text support">
					Already have an account? <a href="/#/login">Sing in</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
        data () {
            return {
                name : "",
                nickname : "",
                email : "",
                password : "",
                filling : [ false , false , false , false ]  
            }
        },
        methods : {
        	changeName(index , name ) {
        		if (this[name] != "") {
        			this.filling[index] = true 
        		}
        		else {
        			this.filling[index] = false
        		}
        	}
        }
    }
</script>

<style scoped>
@font-face 
{
    font-family: 'Nunito', sans-serif;
    src: url(https://fonts.googleapis.com/css?family=Nunito);
}


body
{
	background-color: white;
}
/*@font-face 
{
    font-family: 'Roboto', sans-serif;
    src: url(https://fonts.googleapis.com/css?family=Roboto);
}*/

.registration
{
	left : 20px;
	top: 20px;
	position: absolute;
	background-color: #F5F5F5;
	height: 350px;
	width: 700px;
	border-radius: 9px;
}

.left 
{
	float: left;
	width: 290px;
	height: 350px;
	background-image: url(./img/fon.jpg); 
	background-position: center;
	background-size: cover;
	border-radius: 9px 0px 0px 9px;
}

.right 
{
	float: right;
	width: 410px;
	height: 350px;
}

.text 
{
    font-family: 'Nunito', sans-serif;
    cursor: default;
}

.sign 
{
	position: relative;
	text-align: center;
	top: 40%;
	color: white;
	font-size: 30pt;
}

.input-div
{
	margin: 0% 25% 0% 25%;
}

.input-sub-div
{
	padding-top: 30px;
}

.input
{
	position: relative;
	border: 0px;
	outline: 0;
	top: 20px;
	width: 100%;
	border-bottom: 1px solid #828282;
	background-color: #F5F5F5;
	color: #828282;
	font-size: 12pt;
	transition: 0.3s;
}

.input:focus
{
	border-bottom: 1px solid #1F6A94;
	color: #1F6A94;
	transition: 0.3s;
}

.name-input
{
	position: relative;
	top:-4px;
	width: 50px;
	height: 0px;
	transition: 0.3s;
	
	color: #828282;

}

.input:focus ~ .name-input 
{
	top: -18px;
	transition: 0.3s;
	font-size: 8pt;
	color: #1F6A94;
}


.name-up
{
	top: -18px;
	transition: 0.3s;
	font-size: 8pt;
}

.start
{
	position: relative;
	top: 40px;
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

.support
{
	color : #828282;
	position: relative;
	text-align: center;
	font-size: 9pt;
	top: 5px;
}

</style>