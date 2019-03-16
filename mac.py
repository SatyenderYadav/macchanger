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
wifi=False
ether=False
al=True

try:
	for i in sys.argv:
		if i=='-m':
			mac=sys.argv[sys.argv.index(i)+1]
		if i=='-w':
			wifi=True
			al=False
		if i=='-e':
			ether=True
			al=False

except Exception as e:
	pass

if mac is None:
	mac=rengen()

s=os.popen('ifconfig').read()
s=s.split('\n\n')
name=[]
if ether or al:
	ethname=s[0].split(':')[0]
	name.append(ethname)
if wifi or al:
	wifiname=s[2].split(':')[0]
	name.append(wifiname)
#print(name)
for i in name:
	cmd='echo \''+yourpassword+'\' | sudo -S ip link set dev '+i+' down; echo \''+yourpassword+'\' | sudo -S ip link set dev '+i+' address '+mac+'; echo \''+yourpassword+'\' | sudo -S ip link set dev '+i+' up'
	#print(cmd)
	res=os.popen(cmd).read()
	if res=='':
		print("Mac address of "+i+" set to "+mac)
	mac=rengen()
