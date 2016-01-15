__author__ = 'ndachev'

import sys
sys.path.insert(0, r'./libs')
import pyautogui


# http://rosettacode.org/wiki/Simulate_input/Keyboard#Python

pyautogui.typewrite('Hello world!')
pyautogui.press('enter')  # press the Enter key
