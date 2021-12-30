# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:45:26 2021

Code to check for presence of Chrome download resume button
every 5 seconds (and if found, click on it)

In the meantime, the code 'listens' for a keypress every
0.1 seconds and exits if 'q' is pressed
"""

import keyboard
import sys
import time
import rpa


rpa.init(visual_automation = True, chrome_browser = False)

while True:
    
    try:
        
        rpa.click('resume.png')
        
    except:
        
        x = time.time()
        while time.time() < x+5:
            if keyboard.is_pressed("q"):
                rpa.close()
                sys.exit()
            time.sleep(0.1)