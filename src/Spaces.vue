<template>
    <div class="spaces">
        <div class="option" v-on:click="openSpaces" v-if='statusEmpty'>
            <img class="icon" v-bind:src="spaces[active].img">
            <div class="center text"> {{ spaces[active].name }} </div>
            <img v-if="open" class="arrow" src="./icon/Up.svg"> 
            <img v-else class="arrow up" src="./icon/Up.svg">
            <div class="v-line"></div>
        </div>
        <div v-else>
            <div class="option" v-on:click='openAdding'> 
                <img class="icon" src="./icon/Plus.svg">
                <div class="center text"> New Space </div>
                <div class="v-line"></div>
            </div>
        </div>

        <div class="button-setting" v-on:click="showSetting">
            <div class="text space-setting-text"> Настройки </div>
        </div>

        <div class="space-setting" v-if="setting">
            <div class="elem">
                <div class='text'>Название Space</div>
                <input type="text" class="space-input" v-model="newSpaceName" >
            </div>
            <div class="elem">
                <div class='text'> Участники </div>
                <div class="users">
                    <div class='user' v-for="user in users">
                        <div class="ava"> 
                            <img v-bind:src="user.avatar">
                        </div> 
                        <div class="nickname">
                            {{ user.name }} {{ user.nickname }}
                        </div>
                        <div class='delete' v-on:click="deleteUser(user.nickname)">
                            <img class="icon" src="./icon/Delete.svg">
                        </div>
                    </div>
                </div>
            </div>
            <div class="elem">
                <div class="text">Никнейм нового участника</div>
                <input type="text" class="space-input" v-model="newuser">
                <button class="addUser-btn" v-on:click="addUser"> Пригласить </button>
                <button class="deleteSpace-btn" v-on:click="deleteSpace"> Удалить space </button>
                <button class="saveSpace-btn" v-on:click="saveName"> Сохранить </button>
            </div>
        </div>

        <hr noshade color="white">
        <div v-if="open">
            <div class="option" v-on:click="choiceSpace(index);$emit('choice' , space.id )" 
                                v-for="( space , index ) in spaces" >
                <img class="icon" v-bind:src="space.img">
                <div class="center text"> {{ space.name }} </div>
            </div>
            <hr color="white">
            <div class="option" v-on:click='openAdding'> 
                <img class="icon" src="./icon/Plus.svg">
                <div class="center text"> New Space </div>
            </div>
        </div>

        <div class="addSpace" v-if="adding">
            <center><div class='text'>Новый Space</div></center>
        
            <div class="elem">
                <div class='text'>Название Space</div>
                <input type="text" class="space-input-new" v-model="name">
            </div>    
            <div class="elem">
                <div class='text'>Иконка space</div>
                <div class="input-icon">
                    <label>
                        <input type="file" ref="icon" v-on:change="changePathIcon">
                        <span >Выберите файл</span>
                    </label>
                    <div class='text name-icon'>
                        {{ icon }}
                    </div>
                </div>
            </div>
            <button class="addSpace-btn" v-on:click="addSpace"> Создать Space </button>
            <div class="option"> </div>
            <hr noshade color="white">
            <div class="option" v-on:click="backToSpace"> 
                <img class="icon" src="./icon/left.svg">
                <div class="center text"> Назад </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    props : ["spaces"],
    data () {
        return {
            active : 0, 
            open : false,
            name : "",
            icon : "",
            adding: false,
            setting : false,
            activeSpace : "",
            newuser : "",
            users : [],
            newSpaceName : ""
        }
    },
    methods : {
        choiceSpace( index ) {
            this.active = index
            this.open = false 
            this.loadSpaceUsers()
        },
        openSpaces(){
            this.open = !this.open
            this.adding = false
            this.setting = false 
        },
        changePathIcon(file){
            this.icon = this.$refs.icon.files[0]['name']
        },
        addSpace(){
            self = this 
            axios.post("http://localhost:5000/addspace", {
                cookie : this.$cookie.get('cookie'), 
                name : self.name,
                icon : self.icon 
            }).then(function(argument) {
                self.name = ""
                self.icon = ""
                self.adding = false
                self.open = true 
                self.$emit("reload")
            })
        },
        openAdding(){
            this.open = false
            this.adding = true
            this.name = ""
            this.icon = "" 
        },
        backToSpace(){
            if ( this.statusEmpty)
            {
                this.open = true
            }
            this.adding = false 
            this.name = ""
            this.icon = ""
        },
        showSetting(){
            this.setting = !this.setting
            this.adding = false
            this.open = false 
            this.newSpaceName = this.spaces[this.active].name 
        },
        loadSpaceUsers(){
            self = this 
            axios.post("http://localhost:5000/getspaceusers", {
                cookie : this.$cookie.get('cookie'), 
                id_space : 0 
            }).then(function(argument) {
                console.log(argument.data)
                self.users = argument.data['users']
            })
        },
        addUser(){
            self = this 
            axios.post("http://localhost:5000/adduser", {
                cookie : this.$cookie.get('cookie'), 
                name : self.newuser 
            }).then(function(argument) {
                self.newuser = ""
                self.loadSpaceUsers()
            })
        },
        deleteUser(nickname){
            self = this 
            axios.post("http://localhost:5000/deleteuser", {
                cookie : this.$cookie.get('cookie'), 
                nickname : nickname
            }).then(function(argument) {
                self.loadSpaceUsers()
            })
        },
        saveName(){
            console.log()
            self = this 
            axios.post("http://localhost:5000/save", {
                cookie : this.$cookie.get('cookie'), 
                name : self.newSpaceName,
                id : self.active
            }).then(function(argument) {
                self.setting = false 
                self.$emit("reload")
            })
        },
        deleteSpace(){
            self = this 
            axios.post("http://localhost:5000/deletespace", {
                cookie : this.$cookie.get('cookie'), 
                id : self.active
            }).then(function(argument) {
                self.active = 0
                self.setting = false 

                

                if ( self.spaces.length == 1 ){
                    self.$emit("reload").$emit("choice" , -1)
                }
                else{
                    self.$emit("reload").$emit("choice" , self.spaces[0]['id']) 
                }

                console.log("Hello", self.spaces.length)
                
                console.log("Hello", self.spaces.length)
            })
        }
    },
    computed : {
        statusEmpty(){
            return this.spaces.length !== 0 
        }
    },
    created : function(){
        loadSpaceUsers()
    }
}
</script>

<style scoped>
@font-face 
{
    font-family: 'Roboto', sans-serif;
    src: url(https://fonts.googleapis.com/css?family=Roboto);
}

.spaces
{
    z-index: 100;
    position: absolute;
}

.option /*Ячейка со спейсом и иконкой*/ 
{
    transition: 0.5s;
    background-color: #2D9CDB;
    color: white;
    width: 250px;
    height: 50px;
    transition : 0.2s;
    transform: translateX(30);
}

.option:hover /*Ячейка со спейсом и иконкой*/ 
{
    transition: 0.5s;
    background-color: white;
    width: 250px;
    height: 50px;
    transition : 0.2s;
    transform: translateX(30);
    color: #2D9CDB;
}

.button-setting
{
    position: absolute;
    transition: 0.5s;
    background-color: #2D9CDB;
    color: white;
    top: 0px;
    left: 250px;
    width: 100px;
    height: 50px;
    transition : 0.2s;
}

.button-setting:hover
{
    background-color: white;
    color: #2D9CDB;
}

.space-setting
{
    position: absolute;
    width: 300px;
    height: 500px;
    background-color: #2D9CDB;
    left: 252px;
    top: 52px;
    color: white;
}

.users
{
    position: relative;
    width: 280px;
    height: 200px;
    background-color: white;
    overflow-y: scroll;
}

.user
{
    position: relative;
    width: 100%;
    height: 30px;
    font-family: 'Roboto', sans-serif;
    cursor: default;
    font-size: 10pt;
}

.delete 
{
    position: absolute;
    display: inline-block;
    top: -5px;
    right: 40px;
    cursor: pointer;
}

.center /*Текст внутри ячейки */
{
    position: relative;
    float: left;
    left : 70px;
    top: 16px;
    text-align: center;
}

.space-setting-text
{
    position: relative;
    top: 16px;
    left: 10px;
}

.nickname
{
    position: relative;
    color: black;
    display: inline-block;
    font-family: 'Roboto', sans-serif;
    cursor: default;
    top: -8px;
    left: 20px;
}

.text
{
    font-family: 'Roboto', sans-serif;
    cursor: default;
}

.grey_text /* Ненаведенный текст в ячейке */
{
    color: #DDD;
}

.grey_text:hover /* Наведенный текст в ячейке */
{
    color: white;
}

.icon /*Иконка внутри ячейки*/
{
    position: relative;
    float: left;
    left : 20px;
    top: 11px;
    width: 25px;
    height: 25px;
}

.arrow /* Стрелка вних-вверх */
{
    transition : 0.5s;
    position: relative;
    float: right;
    right : 10px;
    top: 11px;
    fill: #FFF;
    width: 25px;
    height: 25px;
}

.up /* Поворот стрелки */
{
    transition : 0.5s;
    transform: rotate(180deg);
}

.v-line
{
    position: absolute;
    background-color: #FFFFFF;
    width: 2px;
    height: 50px;
    float : right ;
    right: -2px;
    z-index: 400;
}

.addSpace
{
    position: relative;
    width: 250px;
    height: 250px;
    background-color: #2D9CDB;
    padding-top: 10px;
    color: white;
}

.elem
{
    padding-top:20px;
    margin-left: 10px;
}

.space-input 
{
    width: 280px;
    border: 0px;
    outline: 0;
    border-bottom: 2px solid white;
    background-color: #2D9CDB;
    color: white;
    font-size: 14pt;
}

.space-input-new
{
    width: 230px;
    border: 0px;
    outline: 0;
    border-bottom: 2px solid white;
    background-color: #2D9CDB;
    color: white;
    font-size: 14pt;
} 

.addSpace-btn
{
    position: relative;
    background: #2D9CDB;
    border: 1px solid white;
    border-radius: 5px;
    width: 210px;
    height: 40px;
    font-family: 'Roboto', sans-serif;
    font-size: 12pt;
    color: white;
    transition: 0.1s;
    top: 40px;
    left: 20px;
}

.addSpace-btn:hover
{
    background: #F5F5F5;
    border: 1px solid #2D9CDB;
    color: #2D9CDB;
    transition: 0.1s;
}

.deleteSpace-btn
{
    position: relative;
    background: #2D9CDB;
    border: 1px solid white;
    border-radius: 5px;
    width: 120px;
    height: 40px;
    font-family: 'Roboto', sans-serif;
    font-size: 10pt;
    color: white;
    transition: 0.1s;
    top: 80px;
    left: 0px;
}

.deleteSpace-btn:hover
{
    background: #F5F5F5;
    border: 1px solid #2D9CDB;
    color: #2D9CDB;
    transition: 0.1s
}

.saveSpace-btn
{
    position: relative;
    background: #2D9CDB;
    border: 1px solid white;
    border-radius: 5px;
    width: 120px;
    height: 40px;
    font-family: 'Roboto', sans-serif;
    font-size: 10pt;
    color: white;
    transition: 0.1s;
    top: 80px;
    left: 35px;
}

.saveSpace-btn:hover
{
    background: #F5F5F5;
    border: 1px solid #2D9CDB;
    color: #2D9CDB;
    transition: 0.1s
}

.addUser-btn
{
    position: absolute;
    background: #2D9CDB;
    border: 1px solid white;
    border-radius: 5px;
    width: 120px;
    height: 40px;
    font-family: 'Roboto', sans-serif;
    font-size: 10pt;
    color: white;
    transition: 0.1s;
    bottom: 85px;
    right: 10px;
}

.addUser-btn:hover
{
    background: #F5F5F5;
    border: 1px solid #2D9CDB;
    color: #2D9CDB;
    transition: 0.1s
}

.input-icon input[type="file"]
{
    display: none;
}

.input-icon
{
    position: relative;
    background: #2D9CDB;
    border: 1px solid white;
    border-radius: 5px;
    width: 110px;
    height: 40px;
    color: white;
    font-family: 'Roboto', sans-serif;
}

.input-icon:hover
{
    background: white;
    border: 1px solid #2D9CDB;
    color: #2D9CDB;
}

.input-icon label 
{
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    cursor: pointer;
}

.input-icon span 
{
    position: relative;
    line-height: 40px;
    font-size: 9pt;
    left: 10px;
}

.name-icon
{
    position: relative;
    left: 120px;
    top: 15px;
    font-size: 9pt;
}

.ava 
{
    position: relative;
    border: 2px solid #F5F5F5;
    position: relative;
    display: inline-block;
    width: 25px;
    height: 25px;
    border-radius: 40px;
    overflow: hidden;
    left: 10px;
    top: 1px;
}

.icon 
{
    position: relative;
    float: left;
    left : 15px;
    width: 20px;
    height: 20px;
}


hr /* Белая линия */
{
    position: relative;
    width: 200px;
    margin : 0px;
    z-index: 200px;
}
</style>
