# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 07:59:08 2023

@author: Abdur Rahman F R
"""

import random as a
import time
import pyautogui as gi 
while True:
    x=a.randint(400,700)
    y=a.randint(50,300)
    gi.moveTo(x,y)
    time.sleep(5)
