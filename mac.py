#!/usr/bin/python3
import os
import random
import sys


yourpassword=''


def rengen():
	a='ABCDEF1234567890'
	mc=''
	for i in range(0,6):
		mc+=a[random.randint(0, len(a)-1)]+a[random.randint(0, len(a)-1)]+':'
	return mc[:-1]


mac=None
try:
	if sys.argv[1] is not None:
		mac=sys.argv[1]
except Exception as e:
	pass

if mac is None:
	mac=rengen()

os.system('echo \''+yourpassword+'\' | sudo -S ip link set dev wlp1s0 down; echo \''+yourpassword+'\' | sudo -S ip link set dev wlp1s0 address '+mac+'; echo \''+yourpassword+'\' | sudo -S ip link set dev wlp1s0 up')
print("Mac address set to "+mac)
