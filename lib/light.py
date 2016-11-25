import random
import os
# Comment this line out when running on a standard OS (not RPi)
import RPi.GPIO as GPIO
# Comment this line out when running on a RPi
#from lib import gpio_mock as GPIO


def setup():
    """ Function to setup raspberry pi GPIO mode and warnings. PIN 7 OUT and PIN 15 IN """

    # Setup GPIO on raspberry pi
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    # Tell the program you want to use pin number 15 as the input and pin 7 as output
    GPIO.setup(15, GPIO.IN)  # If no input button connected, comment this line out
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)


def activate_goal_light():
    """ Function to activate GPIO for goal light and Audio clip. """

    # select random audio clip
    # Set random numbers depending on number of audio clips available
    songrandom = random.randint(1, 3)
    # Set pin 7 output at high for goal light ON
    GPIO.output(7, False)
    # Prepare commande to play sound (change file name if needed)
    command_play_song = 'sudo mpg123 -q ./audio/goal_horn_{SongId}.mp3'.format(
        SongId=str(songrandom))
    # Play sound
    os.system(command_play_song)
    # Set pin 7 output at high for goal light OFF
    GPIO.output(7, True)


def cleanup():
    """ Function to cleanup raspberry pi GPIO at end of code """

    # Restore GPIO to default state
    GPIO.cleanup()
    print("GPIO cleaned!")
