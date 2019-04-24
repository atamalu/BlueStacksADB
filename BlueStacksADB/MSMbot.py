import subprocess
import os
import random
from time import sleep
from math import pi, cos, sin, sqrt
import re
import json

### Load options for characters
with open('character_options.json', encoding='utf-8') as char_options:
    char_options = json.loads(char_options.read())

### Load coordinates
with open('coordinates.json', encoding='utf-8') as coords:
	coords = json.loads(coords.read())

################
####Settings####
################

package_name = 'com.nexon.maplem.global'

EmuExeName = 'Bluestacks.exe'
EmuExePath = os.getcwd()
EmuExe = f'{EmuExePath}\\{EmuExeName}'

### send commands to emulator adb
AdbExeName = 'HD-Adb.exe'
AdbExePath = os.getcwd()
AdbExe = f'{AdbExePath}\\{AdbExeName}'

# make dictionaries to save info for future use
fl_dict = {
	"Emu Exe Name":EmuExeName,
	"Emu Exe File":EmuExe,
	"Emu Exe Folder":EmuExePath,
	"ADB Exe Name":AdbExeName,
	"ADB Exe Folder":AdbExePath,
	"ADB Exe File":AdbExe
}

from BlueStacksFuncs import adb_connect, adb_shell, adb_keyevent, adb_tap, adb_tap_region, device_list

#############################################################################################################

def elite_dungeon(num_chars = 7):
	
	### Loop until tickets are out
		
	char_range = int(num_chars) + 1

	for char_num in range(1, char_range):
		
		num_tickets = char_options[f"CHARACTER {char_num}"][0]["elite dungeon"][0]["tickets"]
		difficulty = char_options[f"CHARACTER {char_num}"][0]["elite dungeon"][0]["difficulty"]
		completion_time = char_options[f"CHARACTER {char_num}"][0]["elite dungeon"][0]["completion time"]
		
		iter = 1
		
		while num_tickets > 0:
		
			### Tap on character
			adb_tap_region(*coords["select character menu"][0][f"char {char_num}"]) # select char
			sleep(random.randint(3, 4))
			
			### Tap on start
			adb_tap_region(*coords["select character menu"][0]["start"]) # hit start
			sleep(random.randint(10, 12))
			
			### Tap on dungeons icon
			adb_tap_region(*coords["main screen"][0]["dungeons icon"])
			sleep(random.randint(11, 13))
			
			### Tap on elite dungeon graphic
			adb_tap_region(*coords["dungeons menu"][0]["dungeon 1"])
			sleep(random.randint(11, 13))
			
			### Select difficulty
			usediff = f"difficulty {difficulty}"
			adb_tap_region(*coords["elite dungeon menu"][0][usediff])
			sleep(random.randint(7, 8))

			print(f'Starting elite dungeon with ticket {iter}')

			### Create dungeon
			adb_tap_region(*coords["create dungeon"])
			sleep(random.randint(11, 13))
			
			### Start dungeon
			adb_tap_region(*coords["start dungeon"])
			sleep(random.randint(11, 13))
			
			### Auto battle
			adb_tap_region(*coords["main screen"][0]["auto battle"])
			upper_range = completion_time + 20
			sleep(random.randint(completion_time, upper_range))
			
			### Go to menu
			adb_tap_region(*coords["dungeon finished"][0]["go to menu"])
			sleep(random.randint(11, 13))

			print(f'Completed elite dungeon {iter} times')

			num_tickets = num_tickets - 1
			iter = iter + 1
			
			### ignore character if both number of tickets and completion time are 0
			if num_tickets == 0 and completion_time > 0:
			
				##### Execute after tickets run out (keep this here)
				adb_tap_region(*coords["elite dungeon menu"][0]["X button"])
				sleep(random.randint(7, 8))
		
				### Go to full menu and select character
				adb_tap_region(*coords["access full menu"])
				sleep(random.randint(6, 7))
		
				### Enter options
				adb_tap_region(*coords["full menu"][0]["options"])
				sleep(random.randint(6, 7))
		
				### Select character
				adb_tap_region(*coords["options menu"][0]["select character"])
				sleep(random.randint(16, 19))
			else:
				pass
	
		
	
########################################################################## Execute ##########################################################################

### Connect to adb
emu_ips = device_list() # connect to auto-made server
emu_ips = emu_ips[0]
fl_dict['Emu IP'] = emu_ips[1:]

sleep(5)

############################# - - - - - -
	
elite_dungeon()
