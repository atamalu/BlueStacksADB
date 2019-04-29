--- 1-time Setup: ---

[Only tested on Windows 10 in administrator mode, should work on all Windows and maybe Linux/MacOS]

1. Install BlueStacks 4
2. Copy Bluestacks.exe (typically in C:\ProgramData folder) into C:\Program Files\BlueStacks\ (or wherever BlueStacks folder & Hd-Adb.exe is)
3. Install python 3.7+ (programming language it was written in)
4. Copy python.exe into the BlueStacks folder
5. Copy MSMbot.py and .json files into the BlueStacks folder
6. Enable Adb on BlueStacks options and restart BlueStacks
- root BlueStacks and restart here if usage steps 1-3 don't work
7. Set BlueStacks to 1280x720
- 240 dpi and direct-x mode if you want to be safe
8. Reorder dungeons to (tap MSM reorder tab): 1 = elite dungeon, 2 = daily, 3 = mu lung

--- Usage instructions ---

1. Make any wanted changes to character options file in notepad (optional after first time)
2. In MSM, go to character selection screen
3. Execute MSMbot.py and follow the instructions on the prompt
- if running the script just opens and closes a window, 
- hold shift and right-click anywhere in the BlueStacks folder 
- then select Windows PowerShell or whatever and type "python MSMbot.py" 
4. ?????
5. Profit


--- character_options.json file ---

- Change number of tickets, difficulty, and completion time to fit each character
- Change both # of tickets and completion time to 0 to skip a character

--- Notes ---

- Does character selection in order: top-left to top-right, then bottom-left to bottom-right
- Can only do one type of dungeon at a time










--- Other files: ---

--- coordinates.json file

- don't mess with this
- contains icon/menu/etc. pixel coordinates
