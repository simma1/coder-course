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
    print('counter: {}'.format(counter))
    for again in range (0,8):
        print('again: {}'.format(again))

        pa.hotkey('ctrl', 't')
        print('new tab')
        time.sleep(1)
        pa.typewrite('https://www.ecosia.org/%27')
        pa.hotkey('enter')
        time.sleep(3)
        pa.typewrite('ads')
        pa.hotkey('enter')
        time.sleep(3)
        pa.moveTo(412,260, duration = 0.2)
        pa.click()
        time.sleep(1)
        pa.click()