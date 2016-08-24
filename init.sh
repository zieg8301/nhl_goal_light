#!/bin/bash


# basic update 
sudo apt-get -y --force-yes update
read -p "Do you want to DIST-upgrade?" yn
case $yn in
  [Yy]* ) sudo apt-get -y --force-yes dist-upgrade;;
  [Nn]* ) sudo apt-get -y --force-yes upgrade;;
  * ) echo "Please answer yes or no.";;
esac

#raspi-config

#rpi-monitor
sudo wget http://goo.gl/vewCLL -O /etc/apt/sources.list.d/rpimonitor.list
sudo apt-get update
sudo apt-get install rpimonitor -y
sudo /etc/init.d/rpimonitor install_auto_package_status_update

#NHL_Goal_Light_GIT
git clone https://github.com/arim215/nhl_goal_light.git

#reboot
sudo reboot
