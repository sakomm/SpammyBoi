'''
import pyautogui

script = 'you should have picked mercyyyyyy you should have picked any kind of support'

for x in range(30000000):
	x = 10

for x in script.split():
	pyautogui.press("r")
	pyautogui.write(x)
	pyautogui.press("enter")
'''

import pyautogui as pyg
import time

screenWidth, screenHeight = pyg.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyg.position() # Returns two integers, the x and y of the mouse cursor's current position.

inputText = "This is a test i need it to be a lot longer to work uwu iwi"
inputArr = inputText.split()

for word in inputArr:
	pyg.moveTo(276, 877) # Move the mouse to the x, y coordinates 100, 150.
	pyg.click() # Click the mouse at its current location.
	pyg.write(word)
	pyg.moveTo(655,901)
	pyg.click()
	time.sleep(.05)

# 276/877
# 655/901