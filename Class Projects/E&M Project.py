import RPi.GPIO as GPIO
import time
import dweepy

print("Hi. To get started please enter the minimum distance before the buzzer goes off")
limit = int(input())
print("Setup has been completed. Your limit is ", limit)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
buzzer = 17
redLED = 27
greenLED = 22
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(redLED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(greenLED, GPIO.OUT, initial=GPIO.LOW)

def setPing():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        startTime = time.time()
    
    while GPIO.input(ECHO) == 1:
        stopTime = time.time()
        
    timeElapsed = stopTime - startTime
    
    distance = (timeElapsed * 34300) / 2
    distance = round(distance, 2)
    
    return distance
    
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(0.5)
    
while True:
    d = setPing()
    
    if d < limit:
        GPIO.output(buzzer, GPIO.HIGH)
        while True:
            GPIO.output(redLED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(redLED, GPIO.HIGH)
    else:
        GPIO.output(buzzer, GPIO.LOW)
        while True:
            GPIO.output(greenLED, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(greenLED, GPIO.HIGH)
        
    print ('Distance = '), d, ('cm')
    
    buzzerStatus = GPIO.input(17)
    
    if buzzerStatus == True:
        buzzerSignal = True
    else:
        buzzerSignal = False
    
    iot_data = {'Distance': d,'systemName':'Front Gate Detection System','Buzzer': buzzerSignal}
    dweepy.dweet_for('distance_mark10', iot_data)
    time.sleep(0.1)

GPIO.cleanup()
