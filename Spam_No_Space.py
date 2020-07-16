import pyautogui
import time

script = 'you should have picked mercyyyyyy you should have picked any kind of support'
time.sleep(2)
for x in range(30000000):
	x = 10

for x in script.split():
	time.sleep(1)
	pyautogui.press("r")
	pyautogui.write(x)
	for x in range(30000):
		x = 10
	pyautogui.keyDown("ctrl")
	pyautogui.press("enter")
	pyautogui.keyUp("ctrl")

