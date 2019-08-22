# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time
import atexit
# 这个类表示单个的SG90模块
 
 
class Steering:
    max_delay = 0.2
    min_delay = 0.04
 
    def __init__(self, channel, init_position, min_angle, max_angle, speed):
        self.channel = channel
        self.init_position = init_position
        self.position = init_position
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.speed = speed
 
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel, GPIO.OUT, initial=False)
 
        self.pwm = GPIO.PWM(self.channel, 50)  # PWM
        self.pwm.start(2.5 + 10 * self.position / 180)  # 让舵机转到初始位置
        time.sleep(Steering.max_delay)
        self.pwm.ChangeDutyCycle(0)  # 如果不加的话，舵机会不规则抖动
        time.sleep(Steering.min_delay)
 
    def forwardRotation(self):
        print("current position: " + str(self.position))
        if (self.position + self.speed) <= self.max_angle:
            self.position = self.position + self.speed
            self.pwm.ChangeDutyCycle(2.5 + 10 * self.position / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)
        print("current position: " + str(self.position))

            
    def reverseRotation(self):
        print("current position: " + str(self.position))
        if (self.position - self.speed) >= self.min_angle:
            self.position = self.position - self.speed
            self.pwm.ChangeDutyCycle(2.5 + 10 * self.position / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)
        print("current position: " + str(self.position))
            
    def reset(self):
        '''
        Reset the steering to the middle
        '''
        self.position = self.init_position
        self.pwm.start(2.5 + 10 * self.init_position / 180)  # 让舵机转到初始位置
        time.sleep(Steering.max_delay)
        self.pwm.ChangeDutyCycle(0)  # 如果不加的话，舵机会不规则抖动
        time.sleep(Steering.min_delay)
        
 
 
if __name__ == "__main__":
    steer = Steering(38, 90, 45, 136, 5)
    while True:
        direction = input("Please input direction: ")
        if direction == "F":
            steer.forwardRotation()
        elif direction == "R":
            steer.reverseRotation()
        elif direction == "G":
            steer.reset()
