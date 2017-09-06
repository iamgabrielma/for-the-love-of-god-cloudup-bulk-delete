import os
import time
from cloudupdata import username, password, imagesToDelete
from selenium import webdriver

browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))

# Login screen

browser.get('https://cloudup.com/dashboard')
browser.find_element_by_name('username').send_keys(username)
browser.find_element_by_name('pass').send_keys(password)
browser.find_element_by_xpath('//*[@id="login"]/form/div[3]/button').click()
time.sleep(3)

## The party starts here:

count = 0
while count < imagesToDelete:
     
	browser.find_element_by_class_name('col-inner').click()
	print('Deleting image:' + str(count) + ' - ' + browser.current_url + '...')
	time.sleep(1)

	browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/a').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/a').click()
	print(browser.current_url + ' deleted successfully')
	browser.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/form/button').click()
	time.sleep(1)
	count += 1 
