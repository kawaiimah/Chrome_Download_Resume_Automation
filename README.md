# Chrome_Download_Resume_Automation
I had a simple automation problem - when downloading large files from a misbehaving server, I often have to click on the 'resume' button in Chrome. So, I wrote a bit of simple code to check if the 'resume' button is visible on screen every 5 seconds (and if so, click on it!). This allows me to ensure the download resumes even when I'm AFK or asleep overnight.

## Coding Concepts
- Version 1 uses my usual go-to library for such automation situations - pyautogui
- Version 2 uses the python rpa library which among others leverages Tagui from AI Singapore!
- Both versions include a bit of code to wait 5 seconds before checking whether the 'resume' button is on-screen, and in the meantime 'listens' if the key 'q' is pressed which would cause the code to exit.

## Notes
The code snippet to wait for 5 seconds while 'listening' for a keypress feels rather clunky, will continue to keep an eye out for better ways to implement this.
