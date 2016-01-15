__author__ = 'ndachev'

import sys
sys.path.insert(0, r'./libs')
import pyautogui

def ktype(ttext):
   pyautogui.typewrite(ttext)
   pyautogui.press('enter')  # press the Enter key

ktype('test type')

