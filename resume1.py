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
import pyautogui

while True:
    
    try:
        
        x, y = pyautogui.locateCenterOnScreen('resume.png', confidence=0.9)
        pyautogui.click(x, y)
    
    except:
        
        x = time.time()
        print('waiting 5 seconds...')
        while time.time() < x+5:
            if keyboard.is_pressed("q"):
                sys.exit()
            time.sleep(0.1)