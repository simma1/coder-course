import pyautogui as pa

pa.moveTo(425,291, duration=3)
pa.click()
pa.hotkey('ctrl', 'n')
pa.typewrite("print('yee')")
pa.hotkey('ctrl','s')