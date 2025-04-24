#!/usr/bin/env python3
# File name   : init
# Description : Control Servos
# Author      : William
# Date        : 2019/02/23
import time
import board

#from adafruit_motor import servo
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from adafruit_extended_bus import ExtendedI2C as I2C
i2c = I2C(1)

#pwm = PCA9685(i2c,address=int('48',16))
pca = PCA9685(i2c,address=int('5f',16))
pca.frequency = 50
servoA = servo.Servo(pca.channels[0])
servoB = servo.Servo(pca.channels[1])
servoC = servo.Servo(pca.channels[2])
servoD = servo.Servo(pca.channels[3])
servoE = servo.Servo(pca.channels[4])

for i in range(90):
    servoE.angle = i
    time.sleep(0.03)
#for i in range(90):
#    servoE.angle = 90 - i
#    time.sleep(0.03)

pca.deinit()
