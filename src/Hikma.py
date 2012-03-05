#!/usr/bin/env python
#! -*- coding:WINDOWS-1256 -*-
# Hikma.py

import Data
import sys
import time
import os
import random
import pynotify

Par = sys.argv[1]
a = 1

def help() :
	help = """Usage hikma [options]

Options:
-h, --help, Help, help         show this help message and exit
1in1                           show Hikma and exit
1                              show Hikma every 1mn
5                              show Hikma every 5mn
10                             show Hikma every 10mn
15                             show Hikma every 15mn
30                             show Hikma every 30mn
60                             show Hikma every 1h
120                            show Hikma every 2h"""
	print help

if Par == "--h" or Par == 'Help' or Par == 'help' or Par == '--help' :
	help()

elif Par == "1in1" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		notification.show()
		a = 0

elif Par == "1" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		notification.show()
		time.sleep(60)

elif Par == "5" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		notification.show()
		time.sleep(300)

elif Par == "10" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		notification.show()
		time.sleep(600)

elif Par == "15" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		notification.show()
		time.sleep(900)

elif Par == "30" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		notification.show()
		time.sleep(1800)

elif Par == "60" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		notification.show()
		time.sleep(3600)

elif Par == "120" :
	while a :
		pynotify.init("Hikma")
		hikam1 = random.randrange(876)
		hikam = Data.database[hikam1]
		hikamfinal = str(hikam)
		notification = pynotify.Notification("حكمة", hikamfinal, "icons/hikma.png")
		time.sleep(7200)

else :
	print "Error in Program !\nPlease install the program Again !"
