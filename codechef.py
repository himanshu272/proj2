import time 
import sys
import os

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
 
profile = webdriver.FirefoxProfile('/home/himanshu/.mozilla/firefox/bjru6n7m.default')
driver = webdriver.Firefox(executable_path='./geckodriver',firefox_profile=profile)

driver.implicitly_wait(60)

prob_url=sys.argv[1]
code_address=sys.argv[2]

driver.get("https://codechef.com/submit/"+prob_url)
upload=driver.find_element_by_xpath("//input[@type='file']")
upload.send_keys(code_address)

submit=driver.find_element_by_xpath("//input[@id='edit-submit-1']")
driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()
time.sleep(5)
driver.close()


