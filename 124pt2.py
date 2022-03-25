from crypt import methods
from flask import Flask, jsonify, request

app = Flask()
tasks = [{
    'id': 1,
    'Name': 'Sally',
    'Contact': '1010101010',
    'done': False
},
{
    'id': 1,
    'Name': 'Jess',
    'Contact': '2010101010',
    'done': False
}
]

@app.route('/add_data', methods = ['POST'])

def add_task():
    if not request.json:
        return jsonify({'status':'error', 'message': 'please provide data'}, 460)
    
    task = {'id': tasks[-1]['id']+1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact',''),
    'done': False}

    tasks.append(task)
    return jsonify({'status': 'sucess', 'message':'Added sucessfully'})

@app.route('/get_data')
def get_task():
    return jsonify({'data':tasks})

app.run()
