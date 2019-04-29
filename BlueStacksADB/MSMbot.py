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

# go from character screen to main screen
def select_character(char_num):

	### Tap on character
	adb_tap_region(*coords["select character menu"][0][f"char {char_num}"]) # select char
	sleep(random.randint(3, 4))
			
	### Tap on start
	adb_tap_region(*coords["select character menu"][0]["start"]) # hit start
	sleep(random.randint(13, 14))
	
def enter_dungeon(dungeon_code):

	### Tap on main menu icon
	adb_tap_region(*coords["access full menu"])
	sleep(random.randint(3, 4))
			
	### Tap on dungeons icon
	adb_tap_region(*coords["full menu"][0]["dungeons"])
	sleep(random.randint(11, 13))
			
	### Tap on elite dungeon graphic
	adb_tap_region(*coords["dungeons menu"][0][f"dungeon {dungeon_code}"])
	sleep(random.randint(11, 13))
	
def goto_select_character():
	
	### Go to full menu and select character
	adb_tap_region(*coords["access full menu"])
	sleep(random.randint(7, 8))
		
	### Enter options
	adb_tap_region(*coords["full menu"][0]["options"])
	sleep(random.randint(5, 6))
				
	### Tap info tab
	adb_tap_region(*coords["options menu"][0]["info tab"])
	sleep(random.randint(2, 3))
		
	### Select character
	adb_tap_region(*coords["options menu"][0]["select character"])
	sleep(random.randint(16, 19))

def elite_dungeon(num_chars = 7):
		
	char_range = int(num_chars) + 1
	
	# outer loop
	for char_num in range(1, char_range):
	
		### Get character details
		num_tickets = char_options[f"CHARACTER {char_num}"][0]["elite dungeon"][0]["tickets"]
		difficulty = char_options[f"CHARACTER {char_num}"][0]["elite dungeon"][0]["difficulty"]
		completion_time = char_options[f"CHARACTER {char_num}"][0]["elite dungeon"][0]["completion time"]
		
		iter = 1
		
		### Optionally skip over character
		if num_tickets == 0 and completion_time == 0:
			continue
		else:
			pass
		
		### Do until the character runs out of tickets
		while num_tickets > 0:
		
			if iter == 1:
				select_character(char_num)
				enter_dungeon(1)
			else:
				pass
			
			### Select difficulty
			usediff = f"difficulty {difficulty}"
			adb_tap_region(*coords["elite dungeon menu"][0][usediff])
			sleep(random.randint(2, 4))

			print(f'Starting elite dungeon with ticket {iter} for character {char_num}')

			### Create dungeon
			adb_tap_region(*coords["create dungeon"])
			sleep(random.randint(11, 13))
			
			### Start dungeon
			adb_tap_region(*coords["start dungeon"])
			sleep(random.randint(11, 13))
			
			### Auto battle
			adb_tap_region(*coords["main screen"][0]["auto battle"])
			upper_range = completion_time + 10
			sleep(random.randint(completion_time, upper_range))
			
			### Go to menu
			adb_tap_region(*coords["dungeon finished"][0]["go to menu ed"])
			sleep(random.randint(11, 13))
			
			num_tickets = num_tickets - 1
			print(f"Finished dungeon {iter} times, {num_tickets} tickets remaining.")
			iter = iter + 1
		
		### Go to main screen after character is out of tickets
		adb_tap_region(*coords["elite dungeon menu"][0]["X button"])
		sleep(random.randint(3, 4))
		
		### Go to select character
		goto_select_character()
		sleep(random.randint(10, 11))
	
def daily_dungeon(num_chars = 7):
		
	char_range = int(num_chars) + 1
	
	# outer loop
	for char_num in range(1, char_range):
	
		### Get character details
		num_tickets = char_options[f"CHARACTER {char_num}"][0]["daily dungeon"][0]["tickets"]
		difficulty = char_options[f"CHARACTER {char_num}"][0]["daily dungeon"][0]["difficulty"]
		completion_time = char_options[f"CHARACTER {char_num}"][0]["daily dungeon"][0]["completion time"]
		
		iter = 1
		
		### Optionally skip over character
		if num_tickets == 0 and completion_time == 0:
			continue
		else:
			pass
		
		### Do until the character runs out of tickets
		while num_tickets > 0:
		
			if iter == 1:
				select_character(char_num)
				enter_dungeon(6)
			else:
				pass
			
			### Select difficulty
			usediff = f"difficulty {difficulty}"
			adb_tap_region(*coords["daily dungeon menu"][0][usediff])
			sleep(random.randint(2, 4))

			print(f'Starting daily dungeon with ticket {iter} for character {char_num}')

			### Start dungeon
			adb_tap_region(*coords["daily dungeon menu"][0]["enter"])
			sleep(random.randint(8, 10))
			
			### Auto battle
			adb_tap_region(*coords["main screen"][0]["auto battle"])
			upper_range = completion_time + 10
			sleep(random.randint(completion_time, upper_range))
			
			num_tickets = num_tickets - 1 
			
			print(f"Finished dungeon {iter} times, {num_tickets} tickets remaining.")
			iter = iter + 1
		
			if num_tickets == 0:
				### Go to menu
				adb_tap_region(*coords["dungeon finished"][0]["exit dungeon dd"])
				sleep(random.randint(9, 10))
				
				### Go to select character
				sleep(random.randint(3, 4))
				goto_select_character()
				sleep(random.randint(10, 11))
			else:
				### Challenge again 
				adb_tap_region(*coords["dungeon finished"][0]["challenge again dd"])
				sleep(random.randint(11, 13))


	
def mu_lung_dungeon(num_chars = 7):
		
	char_range = int(num_chars) + 1
	
	# outer loop
	for char_num in range(1, char_range):
	
		### Get character details
		num_tickets = char_options[f"CHARACTER {char_num}"][0]["mu lung dungeon"][0]["tickets"]
		completion_time = char_options[f"CHARACTER {char_num}"][0]["mu lung dungeon"][0]["completion time"]
		
		iter = 1
		
		### Optionally skip over character
		if num_tickets == 0 and completion_time == 0:
			continue
		else:
			pass
		
		### Do until the character runs out of tickets
		while num_tickets > 0:
		
			if iter == 1:
				select_character(char_num)
				enter_dungeon(2)
			else:
				pass
			
			print(f'Starting mu lung dungeon with ticket {iter} for character {char_num}')

			### Start dungeon
			adb_tap_region(*coords["daily dungeon menu"][0]["enter"])
			sleep(random.randint(2, 3))
			
			### Confirm that you want to enter the dungeon (?????????)
			adb_tap_region(*coords["mu lung menu"][0]["confirm enter"])
			sleep(random.randint(8, 10))
			
			### Auto battle
			adb_tap_region(*coords["main screen"][0]["auto battle"])
			upper_range = completion_time + 10
			sleep(random.randint(completion_time, upper_range))
			
			num_tickets = num_tickets - 1 
			
			print(f"Finished dungeon {iter} times, {num_tickets} tickets remaining.")
			iter = iter + 1
			
			if num_tickets == 0:
				### Go to menu
				adb_tap_region(*coords["dungeon finished"][0]["exit dungeon ml"])
				sleep(random.randint(11, 13))
		
				### Go to select character
				sleep(random.randint(3, 4))
				goto_select_character()
				sleep(random.randint(10, 11))
			else:
				### Challenge again 
				adb_tap_region(*coords["dungeon finished"][0]["challenge again ml"])
				sleep(random.randint(11, 13))
			
				### Confirm that you want to enter the dungeon AGAIN
				adb_tap_region(*coords["mu lung menu"][0]["confirm enter"])
				sleep(random.randint(4, 5))




########################################################################## Execute ##########################################################################

### Connect to adb
emu_ips = device_list() # connect to auto-made server
emu_ips = emu_ips[0]
fl_dict['Emu IP'] = emu_ips[1:]

sleep(5)

### Get user input
print(f"Codes: \n 1 = elite \n 2 = daily \n 3 = mu lung \n")
duncode = input("Enter number code for dungeon: ")
duncode = int(duncode)

### Read code input
if duncode == 1:
	elite_dungeon()
elif duncode == 2:
	daily_dungeon()
elif duncode == 3:
	mu_lung_dungeon()
else:
	print('Invalid code. Please enter a valid dungeon key.')

###
