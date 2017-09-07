import os
import time
from selenium import webdriver
from optparse import OptionParser

# Variables input:
# python for-the-love-of-god-cloudup-bulk-delete.py -u $YOURUSERNAME -p $YOURPASSWORD

parser = OptionParser()
parser.add_option("-u", "--username", action="store", type="string", dest="username", help="your Cloudup username")
parser.add_option("-p", "--password", action="store", type="string", dest="password", help="your Cloudup password")
parser.add_option("-c", "--count", action="store", type="int", dest="count", default=1000, help="the number of images you want to delete")
(options, args) = parser.parse_args()

# Chrome driver automated browser

browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))

# Login screen

browser.get('https://cloudup.com/dashboard')
browser.find_element_by_name('username').send_keys(options.username)
browser.find_element_by_name('pass').send_keys(options.password)
browser.find_element_by_xpath('//*[@id="login"]/form/div[3]/button').click()
time.sleep(3)

# ## The party starts here:

count = 0
while count < options.count:
    
	browser.find_element_by_class_name('col-inner').click()
	print('Deleting image:' + str(count) + ' - ' + browser.current_url + '...')
	time.sleep(1)
	
	try:
		browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/a').click()
		browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/a').click()
		print(browser.current_url + ' deleted successfully')
		browser.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/form/button').click()
		time.sleep(1)
		count += 1 
	
	except:
		print('Woop! ' + str(count) + ' - ' + browser.current_url + ' was not deleted, will try again soon. Next one!')
		browser.get('https://cloudup.com/dashboard')
		time.sleep(1)
		count += 1