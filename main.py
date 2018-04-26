#coding:utf-8
from flask import Flask, render_template, request, jsonify, json
from flask_cors import CORS, cross_origin
import random
app = Flask(__name__)




spaces = [
    {
      'name' : 'Animals',
      'img' : './src/icon/Animals.svg',
      'id' : 0
    },
    {
      'name' : 'Relocus',
      'img' : './src/icon/Relocus.svg',
      'id' : 1
    }
]
areas = [
  [
    {
      "title": "Abak",
      "projects": [
        {
          "name": "Server",
          "icon": "./src/icon/Server.svg",
          "id" : 0
        },
        {
          "name": "Web app",
          "icon": "./src/icon/Webapp.svg",
          "id": 1
        },
        {
          "name": "Mobile",
          "icon": "./src/icon/Mobile.svg",
          "id": 2
        },
      ]
    },
    {
      "title": "Atlas Volgograd",
      "projects": [
        {
          "name": "Applications",
          "icon": "./src/icon/Applications.svg",
          "id": 3
        },
        {
          "name": "Marketing",
          "icon": "./src/icon/Marketing.svg",
          "id": 4
        },
        {
          "name": "Production",
          "icon": "./src/icon/Production.svg",
          "id": 5
        },
      ]
    },
    {
      "title": "Relocus Tasker",
      "projects": [
        {
          "name": "Server",
          "icon": "./src/icon/Overdue.svg",
          "id": 6
        },
        {
          "name": "Design",
          "icon": "./src/icon/Design.svg",
          "id": 7
        },
        {
          "name": "Development",
          "icon": "./src/icon/Development.svg",
          "id": 8
        },
      ]
    }
  ],
  [
    {
      "title": "Google",
      "projects": [
        {
          "name": "Searching",
          "icon": "./src/icon/Server.svg",
          "id": 10
        },
        {
          "name": "Web app",
          "icon": "./src/icon/Webapp.svg",
          "id": 11
        },
        {
          "name": "Server",
          "icon": "./src/icon/Mobile.svg",
          "id": 12
        },
      ]
    },
    {
      "title": "Atlas Moscow",
      "projects": [
        {
          "name": "Applications",
          "icon": "./src/icon/Applications.svg",
          "id": 13
        },
        {
          "name": "Marketing",
          "icon": "./src/icon/Marketing.svg",
          "id": 14
        },
        {
          "name": "Production",
          "icon": "./src/icon/Production.svg",
          "id":15
        },
      ]
    },
    {
      "title": "Relocus something",
      "projects": [
        {
          "name": "Server",
          "icon": "./src/icon/Overdue.svg",
          "id":16
        },
        {
          "name": "Design",
          "icon": "./src/icon/Design.svg",
          "id":17
        },
        {
          "name": "Development",
          "icon": "./src/icon/Development.svg",
          "id":18
        },
      ]
    }
  ]
]
generals = [[1,2,3],[2,3,4]]
space_id = 0
tasks = [[{
    'name': "The Beggining",
    'area': "Relocus Tasker",
    'project': "Design",
    'members': [
    {
        'name' : "Andrey",
        'nickname' : "Hosstell",
        'avatar' : "./src/img/ava_1.jpg"
    },
    {
        'name' : "Sergey",
        'nickname' : "Pro21",
        'avatar' : "./src//img/ava_2.jpg"
    },
    {
        'name' : "Pavel",
        'nickname' : "SuperNickname",
        'avatar' : "./src/img/ava_3.jpg"
    }
    ],
    'date' : "28 марта",
    'description': "Сбор по поводу проекта в кабинете 2-12 в 12:00",
    'subtasks' : [
        "Обсудить возможный внутрейнний проект",
        "Прототип",
        "Детальный экран главной",
    ],
    'tag' : "Meeting"
},{
    'name' : "Internet Project",
    'area': "Relocus Tasker",
    'project': "Design",
    'members': [
    {
        'name' : "Andrey",
        'nickname' : "Hosstell",
        'avatar' : "./src/img/ava_1.jpg"
    },
    {
        'name' : "Pavel",
        'nickname' : "SuperNickname",
        'avatar' : "./src/img/ava_3.jpg"
    }
    ],
    'date' : "28 марта",
    'description': "Разработка главного проекта нашей компании",
    'subtasks' : [
        "Детальный экран одного проекта",
        "Расписание проeкта в пейпере"
    ],
    'tag' : "Display"
}]]
users = [
    {
        'name': "Andrey",
        'nickname': "Hosstell",
        'avatar': "./src/img/ava_1.jpg"
    },
    {
        'name': "Sergey",
        'nickname': "Pro21",
        'avatar': "./src/img/ava_2.jpg"
    }
]

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGIN'] = 'http://localhost:5000'

@app.route('/login', methods=['GET', 'POST', 'OPTIONS'])
def index():
  if request.method == 'POST':
    return json.dumps({'cookie': 'bestcookie'})
  elif request.method == 'OPTIONS':
    return jsonify('options gg')
  else:
    return json.dumps({'result': 'GET'})


@app.route('/area', methods=['GET', 'POST', 'OPTIONS'])
def index_2():
  if request.method == 'POST':
    print (request.json)
    id_space = request.json['id_space']
    data = {
      'areas' : areas[id_space],
      'general' : generals[id_space]
    }
    return json.dumps(data)
  elif request.method == 'OPTIONS':
    return jsonify('options gg')
  else:
    return json.dumps({'result': 'GET'})

@app.route('/space', methods=['GET', 'POST', 'OPTIONS'])
def index_3():
  if request.method == 'POST':

    return json.dumps({'spaces' : spaces })
  elif request.method == 'OPTIONS':
    return jsonify('options gg')
  else:
    return json.dumps({'result': 'GET'})

@app.route('/tasks', methods=['GET', 'POST', 'OPTION'])
def index_4():
  if request.method == 'POST':
    id_project = request.json['id_project']
    return json.dumps({ 'tasks' : tasks[id_project] })
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})

@app.route('/addspace', methods=['GET', 'POST', 'OPTION'])
def index_5():
  if request.method == 'POST':
    name = request.json['name']
    icon = request.json['icon']
    spaces.append({
        'name' : name,
        'img' : './src/icon/' + icon,
        'id' : random.randint(0,1)
    })

    #print ("Новый спайс")
    #print name , './src/icon/' + icon,
    return json.dumps({ })
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})

@app.route('/getspaceusers', methods=['GET', 'POST', 'OPTION'])
def index_6():
  if request.method == 'POST':

    return json.dumps({ 'users' : users })
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})

@app.route('/adduser', methods=['GET', 'POST', 'OPTION'])
def index_7():
  if request.method == 'POST':
    name = request.json['name']
    print (name)
    users.append({
        'name': "Andrey",
        'nickname': name,
        'avatar': "./src/img/ava_1.jpg"
    })
    return json.dumps({})
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})

@app.route('/deleteuser', methods=['GET', 'POST', 'OPTION'])
def index_8():
  if request.method == 'POST':
    nickname = request.json['nickname']
    for i in range(len(users)):
        if nickname == users[i]["nickname"]:
            del(users[i])
            break
    print (users)
    return json.dumps({})
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})

@app.route('/save', methods=['GET', 'POST', 'OPTION'])
def index_9():
  if request.method == 'POST':
    name = request.json['name']
    id = request.json['id']
    spaces[id]['name'] = name
    return json.dumps({})
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})

@app.route('/deletespace', methods=['GET', 'POST', 'OPTION'])
def index_10():
  if request.method == 'POST':
    id = request.json['id']
    print (id)
    del(spaces[id])
    return json.dumps({})
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})

@app.route('/addarea', methods=['GET', 'POST', 'OPTION'])
def index_11():
  if request.method == 'POST':
    print (request.json)
    name = request.json['name']
    id = request.json['space_id']
    areas[id].append({
        "title" : name,
        "projects" : [ ]
    })

    return json.dumps({})
  elif request.method == 'OPTIONS':
    print('OPTIONS !!')
    return jsonify('options gg')
  else:
    print('GET !!')
    print(request.json)
    print(request.args)
    return json.dumps({'result': 'GET'})



if __name__ == '__main__':
    app.run(debug=True)
