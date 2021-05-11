from motorHelpers import Motor
import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Han!'

@app.route('/forward')
def forward():
    Motor.forward(60)
    return 'ok'

@app.route('/backward')
def backward():
    Motor.backward(60)
    return 'ok'

@app.route('/right')
def right():
    Motor.turnRight(50)
    return 'ok'

@app.route('/left')
def left():
    Motor.turnLeft(50)
    return 'ok'

@app.route('/stop')
def stop():
    Motor.stop()
    return 'ok'

@app.route('/control', methods=["POST"])
def control():
    req = request.json
    if req is None:
        req = json.loads(request.data)
    left = req['left']
    right = req['right']
    if right == 0 and left == 0:
        Motor.stop()
    else:
        Motor.leftMotor(left)
        Motor.rightMotor(right)
    return 'ok'

app.run(host='0.0.0.0', port=2201)