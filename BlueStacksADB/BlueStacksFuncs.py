import subprocess
import os
import random
from time import sleep
from math import pi, cos, sin, sqrt
import re
import json

### Connect to adb

def adb_connect(adb_exe_name="HD-Adb.exe"):
	### Get adb ip
	emuport = subprocess.Popen(f'{adb_exe_name} devices', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
	emuport = emuport.communicate()
	sleep(2)
	emuport = str(emuport)
	emuport = emuport.split('\\')
	emuIP = list(filter(lambda x: 'emulator' in x, emuport))
	# remove leading n
	emuIP = emuIP[0]
	emuIP = emuIP[1:]
	emuport = subprocess.run(f'{adb_exe_name} connect {emuIP}', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	print(emuport)

### Send commands to the adb shell
def adb_shell(cmd, adb_exe_name="HD-Adb.exe", device_ip=''):
	adb_ret = subprocess.run(f'{adb_exe_name} -s {device_ip} shell {cmd}', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	return(adb_ret)

### Enter key commands into android (HOME, BACK, etc.)
def adb_keyevent(key_code):
	adb_ret = adb_shell(cmd = f'input keyevent KEYCODE_{key_code}')
	return(adb_ret)

### Tap position on screen; enter time to hold (ms?);
### 'swipe' same x,y for period of time to mimic holding
def adb_tap(x_coord, y_coord, device_ip='emulator-5554', hold_time=False):
	
	cmd1 = f'input tap {x_coord} {y_coord}'
	if(hold_time == True):
		cmd1 = f'input swipe {x_coord} {y_coord} {x_coord} {y_coord} {hold_time}'
	else:
		pass
	adb_shell(cmd = cmd1, device_ip = device_ip)
	print(f'Tapped screen coordinates: [{x_coord},{y_coord}]')

### Tap random part within a region given a center point and specified radius;
### x, y = center of circle
def adb_tap_region(x, y, radius, device_ip='emulator-5554'):
	
	r_squar, theta = [random.randint(0, radius), 2 * pi * random.random()]
	
	x2 = x + sqrt(r_squar) * cos(theta)
	y2 = y + sqrt(r_squar) * sin(theta)
	adb_tap(x_coord = x2, y_coord = y2, device_ip = device_ip)

### Get list of devices
def device_list(adb_exe_name='HD-Adb.exe'):
	
	devicelist = adb_shell(cmd = 'devices', adb_exe_name = adb_exe_name)
	sleep(2)
	devicelist = str(devicelist)
	devicelist = devicelist.split('\\')
	### Find ports over elements
	devlist = []
	for i in devicelist:
		if re.search("[0-9]{4,5}$", i):
			devlist.append(i)
	return(devlist)

###