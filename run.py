from web.run_script import run_script
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need sudo.")

# jack: Once the GPIO gets triggered, just call run_script() and the proper script will be run :)

# ian: ok let's take a hwhack

#globals:
togl_channel = 69 #i don't actually know these yet. why won't i just look at a pinout already
btn_channel = 42 
dbc_time = 200 #ms

def isr(btn_channel): #interrupt service routine. should be doing as little as humanly possible in here
	if not GPIO.input(togl_channel): #check if armed (toggle low) and fire away
		run_script()

def loop(): #code that runs repeatedly
	btn_state = GPIO.input(btn_channel)
	togl_state = GPIO.input(togl_channel)
	s = "Button state: " + btn_state + " Toggle state: " + togl_state
	print(s) #we don't have to do anything until the button gets pressed so this is just for debug

def setup(togl_channel, btn_channel, dbc_time): #code that runs once
	#yadda yadda yadda input pin inits and internal pullups
	#toggle switch is active low 
	GPIO.setmode(GPIO.BOARD) #using the rpi p1 pinout, no need to go low level
	GPIO.setup(togl_channel, GPIO.IN, pull_up_down=GPIO.PUD_UP) #haha lol pulling your pud
	GPIO.setup(btn_channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(btn_channel, GPIO.FALLING, callback=isr, bouncetime=dbc_time) #falling edge detection with debouncing because polling is for losers

def main(): #gluing it all together

	setup() #first call setup

	while 1:
		loop() #wait for input forever

	GPIO.cleanup() #reset io config
  
if __name__== "__main__":
	main()
