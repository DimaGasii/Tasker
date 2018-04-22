<template>
	<div class="login">
		<div class="left">
			<div class="text sign"> Sign In</div>
		</div>
		<div class="right">
			<div class="input-div">
				<div class="wrong text" v-if="wrong"> Wrong the nickname or the password </div>

				<div class="input-sub-div"> 
					<input type="text" class="input" v-model="nickname" v-on:input="changeName(0,'email')" 
					v-bind:class="{ 'input-wrong' : wrong }">
					<div class="text name-input" v-bind:class="{ 'name-up' : filling[0] }"> Nickname </div>
				</div>
				<div class="input-sub-div"> 
					<input type="password" class="input" v-model="password" v-on:input="changeName(1,'password')"
					v-bind:class="{ 'input-wrong' : wrong }">
					<div class="text name-input" v-bind:class="{ 'name-up' : filling[1] }"> Password </div>
				</div>
			</div>
			<div class="start">
				<button class="btn text" v-on:click="login"> Sign In </button>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios"

export default {
    data () {
        return {
            nickname : "",
            password : "",
            wrong : false,
            filling : [ false , false ]  
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
    	},
    	login(){
    		self = this
    		axios.post("http://192.168.43.142:5000/login", {
    			nickname : this.nickname,
    			password : this.password
    		}).then(function (argument) {
    			let cookie = argument.data['cookie']
    			console.log(argument.data)
    			if ( cookie != null ){
    				self.addCookie(cookie)
    				self.wrong = false
    				self.$router.replace({ name: 'main' }) 
    			}
    			else{
    				self.wrong = true 
    			}
    		}).catch(function (error){
    			console.log(error)
    		})
    	},
    	// check(){
    	// 	axios.post("http://192.168.43.142:5000/", {
    	// 		cookie : this.$cookie.get('cookie')
    	// 	}).then(function (argument) {
    	// 		console.log(argument)
    	// 	}).catch(function (error){
    	// 		console.log(error)
    	// 	})
    	// }
    	addCookie(cookie){
    		this.$cookie.set('cookie', cookie , 356)
    	}
    },
    created : function(){
    	console.log("start")
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

.wrong 
{
	position: absolute;
	font-size: 10pt;
	color: red;
}

.login
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

.text-wrong
{
	color: red;
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
	margin: 13% 25% 0% 25%;
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

.input-wrong
{
	border-bottom: 1px solid red;
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


</style>