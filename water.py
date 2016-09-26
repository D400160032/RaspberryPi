#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
pinList = [16, 17, 18, 27, 22, 5, 6, 13, 19, 26]

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

for i in pinList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.LOW)

while True:
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print "Waitng For Sensor To Settle"
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance >= 20 and distance >= 19:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 18 and distance >= 17:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 16 and distance >= 15:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 14 and distance >= 13:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 12 and distance >= 11:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 10 and distance >= 9:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 8 and distance >= 7:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 6 and distance >= 5:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 4 and distance >= 3:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
  elif distance <= 2 and distance >= 1:
    GPIO.output(pinList, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
