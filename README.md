# nhl_goal_light
Nhl goal light python for raspberry pi GPIO. Works with any team, just enter team name (without city) when prompted.<br/>
Before using this file, make sur you have:

python-pip, python-dev, python-rpi.gpio, mpg123, goal_horn_1.mp3, goal_horn_2.mp3, goal_horn_3.mp3

run: $ sudo apt-get install python-dev python-rpi.gpio mpg123 python-pip<br/>
or run: $ sudo apt-get install mpg123 python-pip<br/>
        $ sudo pip install -r requirements.txt

#Materials<br/>
-Raspberry Pi (using raspberry pi A model, but any model will work. PiZero would be best, but needs GPIO to be installed)<br/>
-Red Rotating Beacon Warning Light from ebay<br/>
-5V 2 Channel Relay Module from ebay<br/>
-Momentary OFF ON Push Round Button<br/>
-12V to 5V 1A adapter (used a car usb adapter)<br/>

#Audio<br/>
If you wish to change the audio clips to sounds with your teams goal horn and music, just download them, rename them (goal_horn_#.mp3) and save them in the "audio" folder.
