# nhl_goal_light

###Overview

Nhl goal light python for raspberry pi GPIO. Works with any team, just enter team name (without city) when prompted.
Before using this file, make sur you have:


python-pip, python-dev, python-rpi.gpio, mpg123, goal_horn_1.mp3, goal_horn_2.mp3, goal_horn_3.mp3

run: 

        $ sudo apt-get install python-dev python-rpi.gpio mpg123 python-pip
or run: 

        $ sudo apt-get install mpg123 python-pip
        $ sudo pip install -r requirements.txt

For documentation on how to wire the GPIOs with the lights and the button, pleaser refer to the "docs" folder.

###Materials

-Raspberry Pi (currently using raspberry pi A model, but any model will work)

-Red Rotating Beacon Warning Light from ebay

-5V 2 Channel Relay Module from ebay

-Momentary OFF ON Push Round Button

-12V to 5V 1A adapter (used a car usb adapter)

-3.5mm audio extension cable

###Audio
If you wish to change the audio clips to sounds with your teams goal horn and music, just download them, rename them (goal_horn_#.mp3) and save them in the "audio" folder.

### TODO
-Test response time after a goal is scored

-create test folder and test files to allow testing with just a raspberry pi
