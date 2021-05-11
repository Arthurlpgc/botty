#!/usr/bin/python
from PCA9685 import PCA9685
import time

Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x43, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        if(motor == 1):
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
 
    
    def stop(self):
        pwm.setDutycycle(self.PWMA, 0)
        pwm.setDutycycle(self.PWMB, 0)

    def forward(self, strength):
        self.MotorRun(0, 'forward', strength)
        self.MotorRun(1, 'forward', strength)

    def backward(self, strength):
        self.MotorRun(0, 'backward', strength)
        self.MotorRun(1, 'backward', strength)

    def turnRight(self, strength):
        self.MotorRun(0, 'forward', strength)
        self.MotorRun(1, 'backward', strength)

    def turnLeft(self, strength):
        self.MotorRun(0, 'backward', strength)
        self.MotorRun(1, 'forward', strength)
    
    def leftMotor(self, strength):
        self.MotorRun(0, 'backward' if strength < 0 else 'forward', abs(strength))

    def rightMotor(self, strength):
        self.MotorRun(1, 'backward' if strength < 0 else 'forward', abs(strength))



Motor = MotorDriver()

strength = 75

def moveFor(tm):
    Motor.forward(strength)
    time.sleep(tm)
    Motor.stop()

def moveBack(tm):
    Motor.backward(strength)
    time.sleep(tm)
    Motor.stop()

def turnRight(tm):
    Motor.turnRight(strength)
    time.sleep(tm)    
    Motor.stop()

def turnLeft(tm):
    Motor.turnLeft(strength)
    time.sleep(tm)    
    Motor.stop()



