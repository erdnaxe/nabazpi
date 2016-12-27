## http://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/

import RPi.GPIO as GPIO

n = 2  # GPIO number

GPIO.setmode(GPIO.BCM)  # Follow broadcom convention

print(GPIO.getmode())  # Print the conf

print("Was configured as ", GPIO.gpio_function(n))
GPIO.setup(n, GPIO.OUT)  # Set as OUT
print("Now configured as ", GPIO.gpio_function(n))

GPIO.output(n, GPIO.HIGH)  # Set as HIGH

