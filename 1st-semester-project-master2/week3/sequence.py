import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

btn = 33
btn2 = 8

l1 = 5
l2 = 37
l3 = 15
l4 = 13

l = [l1, l2, l3, l4]

on = 0
s = 1
next = 1
led_order = 0

def setup():
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l, 1)

    GPIO.setup(btn, GPIO.IN)
    GPIO.setup(btn2, GPIO.IN)

    GPIO.setup([btn, btn2], GPIO.IN, pull_up_down=GPIO.PUD_UP)


def blink(n):
    global led_order

    if led_order > 3:
        led_order = 0
        n = 0

    GPIO.output(l[n], 0)
    sleep(s)
    GPIO.output(l[n], 1)

    led_order += 1

def seq():
    while on:
        blink(led_order)


def turn_on(x=None):
    global on
    on = not on


def speed(x=None):
    global next
    global s

    if next == 3:
        next = 0

    speeds = [1, 0.5, 0.1]
    s = speeds[next]

    next +=1

    print('Current speed: {}'.format(s))

def loop():
    GPIO.add_event_detect(btn, GPIO.RISING, turn_on, bouncetime=200)
    GPIO.add_event_detect(btn2, GPIO.BOTH, speed, bouncetime=100)

    while True:
        seq()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except:
        GPIO.cleanup()
