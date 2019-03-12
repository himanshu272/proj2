import time 
import sys
import os

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

IS_FIREFOX = True
 
if IS_FIREFOX:
	profile = webdriver.FirefoxProfile('/home/himanshu/.mozilla/firefox/bjru6n7m.default')
	driver = webdriver.Firefox(executable_path='./geckodriver',firefox_profile=profile)

else:
	options = webdriver.ChromeOptions()
	options.add_argument('user-data-dir=/home/himanshu/.config/\google-chrome/')
	options.headless = True
	driver = webdriver.Chrome(executable_path = '../chrome/chromedriver', options =options)

driver.implicitly_wait(60)

prob_url=sys.argv[1]
code_address=sys.argv[2]
try:
	driver.get("https://codechef.com/submit/"+prob_url)
	upload=driver.find_element_by_xpath("//input[@type='file']")
	upload.send_keys(code_address)

	submit=driver.find_element_by_xpath("//input[@id='edit-submit-1']")
	driver.execute_script("arguments[0].scrollIntoView();", submit)
	submit.click()
	time.sleep(5)
except Exception as e:
	f = open("error.log","a")
	print("Error occured.\n Check the error.log file")
	f.close()
finally:
	driver.close()


