import RPi.GPIO as GPIO
import time

#We define our GPIO's, using the GPIO.BOARD mode
led_pin = 8
btn_pin = 10
sw_status = 0

#We set LedPin as input and BtnPin as Output in pull up down configuration
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Helper function that changes sw_status from 1 to 0 and vice versa
def switch_state(_=None):
    global sw_status
    sw_status = not sw_status

#This is the core function of the program
def loop():
        GPIO.add_event_detect(btn_pin, GPIO.RISING, switch_state, bouncetime=200) #Listens for when button is raised, if it is raised it calls function switch_state
        led_state = 1 #This is variable that is used for switching between HIGH and LOW output
        while True:
            if sw_status:
                led_state = not led_state #If led_state is 1 this will turn it into 0 and vice versa
                GPIO.output(LedPin, led_state) #Led output, we use the led_state variable to indicate HIGH or LOW
                time.sleep(0.3) #waits for 0.3s before reiterating over the while loop, this allows for the blinking effect
            else:
                GPIO.output(LedPin, 1) #Switches off the led
                pass # Pass == don't do anything

#When the program is ended this will clear GPIO setup settings
def destroy():
	GPIO.output(LedPin, 1)
	GPIO.cleanup()

if __name__ == '__main__':
        setup()
        GPIO.output(led_pin, 1)
        try:        #We use the try/except statement to handle errors, when for whatever reason loop doesn't execute the destroy function will be called instead.
            loop()
        except:
            destroy()
