import time

from adafruit_motor import motor
from adafruit_pca9685 import PCA9685
from adafruit_extended_bus import ExtendedI2C as I2C
i2c = I2C(1)

MOTOR_M1_IN1 =  15      #Define the positive pole of M1
MOTOR_M1_IN2 =  14      #Define the negative pole of M1
MOTOR_M2_IN1 =  12      #Define the positive pole of M2
MOTOR_M2_IN2 =  13      #Define the negative pole of M2
MOTOR_M3_IN1 =  11      #Define the positive pole of M3
MOTOR_M3_IN2 =  10      #Define the negative pole of M3
MOTOR_M4_IN1 =  8       #Define the positive pole of M4
MOTOR_M4_IN2 =  9       #Define the negative pole of M4

pwm_motor = PCA9685(i2c, address=0x5f)
pwm_motor.frequency = 50

def map(x,in_min,in_max,out_min,out_max):
  return (x - in_min)/(in_max - in_min) *(out_max - out_min) +out_min


motor1 = motor.DCMotor(pwm_motor.channels[MOTOR_M1_IN1],pwm_motor.channels[MOTOR_M1_IN2] )
motor1.decay_mode = (motor.SLOW_DECAY)
motor2 = motor.DCMotor(pwm_motor.channels[MOTOR_M2_IN1],pwm_motor.channels[MOTOR_M2_IN2] )
motor2.decay_mode = (motor.SLOW_DECAY)

def Motor(channel,direction,motor_speed):
  if motor_speed > 100:
    motor_speed = 100
  elif motor_speed < 0:
    motor_speed = 0
  speed = map(motor_speed, 0, 100, 0, 1.0)
  if direction == -1:
    speed = -speed

  if channel == 1:
    motor1.throttle = speed
  elif channel == 2:
    motor2.throttle = speed

def motorStop():#Motor stops
    motor1.throttle = 0
    motor2.throttle = 0

def destroy():
  motorStop()
  pwm_motor.deinit()


if __name__ == '__main__':
  try:     
      speed_set = 50
      Motor(1, -1, speed_set)
      Motor(2, -1, speed_set)
      print("Forward")
      time.sleep(2)
      Motor(1, 1 ,speed_set)
      Motor(2, 1, speed_set)
      print("Backward")
      time.sleep(2)
      destroy()
  except KeyboardInterrupt:
    destroy()
