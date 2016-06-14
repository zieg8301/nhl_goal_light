#!/usr/bin/python

import os

def update():
	"""function to update apt."""
	command='sudo apt-get udpate'
	os.system(command)

def upgrade():
	"""function to dist-upgrade with apt."""
	command='sudo apt-get dist-upgrade -y'
	os.system(command)

def install ():
	"""function to install the needed tools."""
	command='sudo apt-get install python-dev python-rpi.gpio mpg123 git rpi-update apt-transport-https ca-certificates -y'
	os.system(command)

def rpi_monitor():
	"""function to install rpi-monitor. Add rpi-monitor to apt update list."""
	command='sudo wget http://goo.gl/rsel0F -O /etc/apt/sources.list.d/rpimonitor.list'
	os.system(command)
	command='sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 2C0D3C0F'
	os.system(command)
	command='sudo apt-get update'
	os.system(command)
	command='sudo apt-get install rpi-monitor -y'
	os.system(command)
	command='sudo /usr/share/rpimonitor/scripts/updatePackagesStatus.pl'
	os.system(command)

def git_nhl():
	"""function to clone nhl_goal_light for github."""
	command='git clone https://github.com/arim215/nhl_goal_light.git'
	os.system(command)
	
def rpi_update():
	"""function to run rpi-update to update kernel."""
	command='sudo rpi-update'
	os.system(command)
	
def reboot():
	"""function to reboot."""
	command='sudo reboot'
	os.system(command)

#MAIN
#init    
print ("Updating and Upgrading")
update()
upgrade()
print ("Installing python-dev python-rpi.gpio mpg123 git rpi-update apt-transport-https ca-certificates")
install_all()
print ("install rpi-monitor")
rpi_monitor()
print ("clone NHL light")
git_nhl()
print ("rpi-update")
rpi_update()
print ("reboot!")
reboot()
