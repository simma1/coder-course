from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
import time

def multiplier(a,b):
	return a*b

opts = Options()
opts.headless = False

assert opts.set_headless
browser = Chrome(
	executable_path='C:/Users/spi59/Documents/Drivers/chromedriver.exe',
	options=opts)

browser.get('https://freerice.com/categories')
time.sleep(0.5)
cookie_monster = browser.find_element_by_class_name('as-js-optin')
cookie_monster.click()
time.sleep(0.5)
categories = browser.find_elements_by_class_name('category-item')
categories[21].click()
time.sleep(2)

for rice_donator in range (1,1000):
	try:
		element = WebDriverWait(browser, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'card-title')))

	except Exception as e:
		pass

	else:
		question = browser.find_element_by_class_name('card-title')
		data = question.text
		split = data.split(" x ")
		A = split[0]
		B = split [1]
		intA = int(A)
		intB = int(B)

		answer = multiplier(intA,intB)

		options = browser.find_elements_by_class_name('card-button.fade-appear-done.fade-enter-done')
		
		opt1 = options[0].text
		opt1int = int(opt1)
	 
		opt2 = options[1].text
		opt2int = int(opt2)
	 
		opt3 = options[2].text
		opt3int = int(opt3)
	 
		opt4 = options[3].text
		opt4int = int(opt4)

		if opt1int == answer:
			options[0].click()
		elif opt2int == answer:
			options[1].click()
		elif opt3int == answer:
			options[2].click()
		elif opt4int == answer:
			options[3].click()

		print(rice_donator * 10)




	