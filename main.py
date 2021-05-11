from motorHelpers import Motor

from flask import Flask
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

app.run(host='0.0.0.0', port=2201)