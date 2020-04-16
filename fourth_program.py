import pyautogui as pa
import time 

pa.hotkey('win')
time.sleep(1)
pa.typewrite('chrome')
time.sleep(1)
pa.hotkey('enter')
time.sleep(4)
pa.moveTo(405,51, duration = 1)
pa.click()

for counter in range (0,10):
	for again in range (0,8):
		pa.hotkey('ctrl', 't')
		time.sleep(1)
		pa.typewrite('https://www.ecosia.org/')
		pa.hotkey('enter')
		time.sleep(3)
		pa.moveTo(206,300, duration = 1)
		pa.click()
		time.sleep(3)
		pa.moveTo(397,509, duration = 1)
		pa.click()
		time.sleep(3)
		pa.typewrite('ads')
		pa.hotkey('enter')
		time.sleep(3)
		pa.moveTo(382,487, duration = 1)
		pa.click()
		time.sleep(3)