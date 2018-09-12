import RPi.GPIO as GPIO
import time

#We set variables according to GPIO pinout
LED = 14
BTN = 5

#Variable to indicate current status - ON/OFF
ON = True

#We create function that sets up the GPIO numbering mode as BCM,
#sets LED gpio as output and button gpio as input
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#switches the status of the ON variable - If ON is True then not ON == False and vice versa.
#If ON == True then the LED will light up.
def switch(ev=None):

    global ON
    ON = not ON

    GPIO.output(LED, ON)

#We create a loop that listents to the event which in our case is the pushing of a button,
#when the event is detected then the method with call its callback function that is switch.
#Bouncetime will prevent callback function being accidentaly called multiple times
def loop():
    GPIO.add_event_detect(BTN, GPIO.FALLING, callback=switch, bouncetime=200)
    while True:
        time.sleep(1)

#We make this function to to serve as error handler, if our loop goes wrong, end gets called
# so the led will turn off and gpio resource will be released.
def end():
    GPIOU.output(LED, GPIO.HIGH)
    GPIO.cleanup()

#When the program is run from the directly from the source file then setup() gets called
# after which we enter into infinite loop that can be interrupted only by error or forcefully exiting the progrma.
if __name__ == '__main__':

    setup()

    try:
        loop()
    except:
        destroy()
