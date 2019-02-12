import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

buttonPin = 16
sensorPin = 18
lightPin = 12
soundSensor = 25

GPIO.setup(sensorPin, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(soundSensor, GPIO.OUT)

try:
    while True:
        p = GPIO.PWM(soundSensor, 50)
        button_state = GPIO.input(buttonPin)
        if GPIO.input(sensorPin):
            GPIO.output(lightPin, 1)
            p.start(50)
            p.ChangeFrequency(300)
            print("Motion Detected")
            time.sleep(0.1)
            GPIO.output(lightPin, 0)
        elif not button_state:
            print("Clicked!")
            GPIO.cleanup()
            os.system("sudo shutdown -h now")
        else:
            GPIO.output(lightPin, 0)
            GPIO.output(soundSensor, 0)
            p.stop()
        time.sleep(0.1)

except:
    GPIO.cleanup()
