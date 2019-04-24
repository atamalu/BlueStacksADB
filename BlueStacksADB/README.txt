--- 1-time Setup: ---

[Only tested on Windows 10 in administrator mode, should work on all Windows and maybe Linux/MacOS]

1. Install BlueStacks 4
2. Copy Bluestacks.exe (typically in C:\ProgramData folder) into C:\Program Files\BlueStacks\ (or wherever BlueStacks folder & Hd-Adb.exe is)
3. Install python 3.7+ (programming language it was written in)
4. Copy edstacks.py and .json files into the BlueStacks folder
5. Right-click edstacks.py and make python.exe the default program to open it (if not already)
- if running the script just opens and closes a window, 
- copy Python into the BlueStacks folder then execute python.exe and type:   exec(open("edstacks.py").read())
6. Enable Adb on BlueStacks options and restart BlueStacks
- root BlueStacks and restart here if usage steps 1-3 don't work
7. Set BlueStacks to 1280x720
- 240 dpi and direct-x mode if you want to be safe


--- Usage instructions ---

1. Make any wanted changes to character options file (optional)
2. In MSM, go to character selection screen
3. Execute edstacks.py 
4. ?????
5. Profit


--- character_options.json file ---

- Elite dungeon only one currently working so ignore rest of options
- Change number of tickets, difficulty, and completion time to fit each character
- Change both # of tickets and completion time to 0 to skip a character


--- Notes ---

- Does ed for characters in order: top-left to top-right, then bottom-left to bottom-right
- Elite dungeon icon must be in 1st dungeon slot










--- Other files: ---

--- coordinates.json file

- don't mess with this
- contains icon/menu/etc. pixel coordinates
