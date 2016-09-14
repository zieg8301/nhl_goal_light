#! /usr/bin/python

import urllib.request
import urllib.parse
import configparser
import smtplib
import os
import datetime as dt
from email.mime.text import MIMEText

"""
Use config file /home/$USER/.hockeytext
"""

config = configparser.ConfigParser()
config.read(os.getenv("HOME") + '/.hockeytext')
email = config.get('config', 'email')
password = config.get('config', 'password')
number = config.get('config', 'number')
carrier = config.get('config', 'carrier')
team = config.get('config', 'team')
tz_offset = config.get('config', 'tz_offset')
tz_offset = int(tz_offset)


def send_text(message):
""" Sends text message to user """
    domains = {'verizon': 'vtext.com', 'att': 'txt.att.net',
               'tmobile': 'tmomail.net', 'sprint': 'messaging.sprintpcs.com',
               'virgin': 'vmobl.com', 'uscellular': 'email.uscc.net',
               'nextel': 'messaging.nextel.com', 'boost': 'myboostmobile.com',
               'alltel': 'message.alltel.com','rogers' : 'sms.rogers.com'}

    domain = domains.get(carrier)
    text_to = number + '@' + domain

    msg = MIMEText(message)
    msg = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, text_to, msg)
    server.quit()

if __name__ == "__main__":
  text = ('Test')
  send_text(text)
  raise SystemExit
