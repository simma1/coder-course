import pyautogui as pa

pa.moveTo(93,102, duration=3)
pa.click()
pa.moveTo(213,227, duration=1)
pa.click()
pa.typewrite('print("success")')