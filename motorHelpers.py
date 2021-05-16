#!/usr/bin/python
from PCA9685 import PCA9685
import time

Dir = [
    'forward',
    'backward',
]
pwm_back = PCA9685(0x43, debug=False)
pwm_back.setPWMFreq(50)
pwm_front = PCA9685(0x40, debug=False)
pwm_front.setPWMFreq(50)

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
            self.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                self.setLevel(self.AIN1, 0)
                self.setLevel(self.AIN2, 1)
            else:
                self.setLevel(self.AIN1, 1)
                self.setLevel(self.AIN2, 0)
        if(motor == 1):
            self.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                self.setLevel(self.BIN1, 0)
                self.setLevel(self.BIN2, 1)
            else:
                self.setLevel(self.BIN1, 1)
                self.setLevel(self.BIN2, 0)
 
    
    def stop(self):
        self.setDutycycle(self.PWMA, 0)
        self.setDutycycle(self.PWMB, 0)

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
    
    def setDutycycle(self, channel, pulse):
        pwm_back.setDutycycle(channel, pulse)
        pwm_front.setDutycycle(channel, pulse)
    
    def setLevel(self, channel, level):
        pwm_back.setLevel(channel, level)
        pwm_front.setLevel(channel, level)



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



