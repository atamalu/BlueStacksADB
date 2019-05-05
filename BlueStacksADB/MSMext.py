import subprocess
import os
import random
from time import sleep
from math import pi, cos, sin, sqrt
import re
import json

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

#####

def start_extract():
    ### Tap on main menu icon
	adb_tap_region(*coords["access full menu"])
	sleep(random.randint(4, 5))

    ### Tap on dungeons icon
	adb_tap_region(*coords["full menu"][0]["shop"])
	sleep(random.randint(4, 5))

    ### Tap on dungeons icon
	adb_tap_region(*coords["full menu"][0]["shop cash shop"])
	sleep(random.randint(4, 5))

    ### Tap on treasure box tab
	adb_tap_region(*coords["cash shop"][0]["treasure box tab"])
	sleep(random.randint(4, 5))

    ### Tap on 'buy 10 + 1' button
	adb_tap_region(*coords["cash shop"][0]["treasure box buy 10"])
	sleep(random.randint(3, 4))

def continue_extract():

    ### Tap on dungeons icon
	adb_tap_region(*coords["full menu"][0]["shop cash shop"])
	sleep(random.randint(4, 5))

    ### Tap on treasure box tab
	adb_tap_region(*coords["cash shop"][0]["treasure box tab"])
	sleep(random.randint(4, 5))

    ### Tap on 'buy 10 + 1' button
	adb_tap_region(*coords["cash shop"][0]["treasure box buy 10"])
	sleep(random.randint(3, 4))

### Start at 'confirm purchase'
def buy_items():
    # confirm you want to buy
    adb_tap_region(*coords["cash shop"][0]["treasure box buy confirm"])
    sleep(random.randint(13, 15))
    
    # open all
    adb_tap_region(*coords["cash shop"][0]["treasure box open all"])
    sleep(random.randint(9, 11))
    
###

def extract_items():
    # at full menu after buying; go to bag
    adb_tap_region(*coords["full menu"][0]["bag"])
    sleep(random.randint(4, 5))

    # go to extract menu
    adb_tap_region(*coords["bag"][0]["extract"])
    sleep(random.randint(4, 5))

    # hit extract button in extract menu
    adb_tap_region(*coords["bag"][0]["extract menu extract"])
    sleep(random.randint(3, 4))

    # confirm extraction
    adb_tap_region(*coords["bag"][0]["extract menu confirm"])
    sleep(random.randint(3, 4))

    # now back at bag; confirm... something?
    adb_tap_region(*coords["bag"][0]["extract menu done confirm"])
    sleep(random.randint(5, 7))

    # hit big X twice to get back to full menu
    adb_tap_region(*coords["elite dungeon menu"][0]["X button"])
    sleep(random.randint(2, 3))
    adb_tap_region(*coords["elite dungeon menu"][0]["X button"])
    sleep(random.randint(2, 3))


from BlueStacksFuncs import adb_connect, adb_shell, adb_keyevent, adb_tap, adb_tap_region, device_list

########################################################################## Execute ##########################################################################

### Connect to adb
emu_ips = device_list() # connect to auto-made server
emu_ips = emu_ips[0]
fl_dict['Emu IP'] = emu_ips[1:]

sleep(5)

### Get user input
num_pulls = input("How many treasure boxes do you want to buy and extract? ")
bag_space_orig = input("How many units of free bag space do you have? ")
num_pulls = int(num_pulls)
bag_space_orig = int(bag_space_orig)

iter = 1
num_items_pulled = 0

while iter <= num_pulls:
    if iter == 1:
        start_extract()
        buy_items()
        bag_space = bag_space_orig - 11
        adb_tap_region(*coords["cash shop"][0]["treasure box use again"])
        sleep(random.randint(9, 11))
        iter = iter + 1
    else:
        if bag_space >= 11:
            buy_items()
            bag_space = bag_space - 11
            adb_tap_region(*coords["cash shop"][0]["treasure box use again"])
            sleep(random.randint(9, 11))
            iter = iter + 1
        else:
            # treasure box cancel (not use again)
            adb_tap_region(*coords["cash shop"][0]["treasure box buy cancel"])
            sleep(random.randint(3, 4))
            # hit X button
            adb_tap_region(*coords["elite dungeon menu"][0]["X button"])
            sleep(random.randint(2, 3))
            # now at full menu
            extract_items()
            bag_space = bag_space_orig
            continue_extract()
            iter = iter + 1
            # command to exit extracting items then donezo
        
        
print(f'Done. Completed {iter} times')
###
