from motorHelpers import Motor
import json
from flask import Flask, request, Response
import picamera 
import cv2
app = Flask(__name__)
vc = cv2.VideoCapture(0) 
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


def gen(): 
   """Video streaming generator function.""" 
   while True: 
       rval, frame = vc.read() 
       cv2.imwrite('pic.jpg', frame) 
       yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n') 

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='0.0.0.0', port=2201)