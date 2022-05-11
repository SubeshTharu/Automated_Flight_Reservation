import os
import time
import logging
from selenium import webdriver

logging.basicConfig(filename='flight.log',format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%y/%m/%d %H:%M:%S', level=logging.INFO, filemode='w')

paths = os.path.join(os.getcwd(),"chromedriver_win32",'chromedriver.exe')
browser = webdriver.Chrome(executable_path= paths)

browser.get('https://www.yetiairlines.com/')
browser.maximize_window()
logging.info('Browser was opened successfully.')
time.sleep(2)


two_way = browser.find_element_by_id('selectMenuTripType')
two_way.click()
time.sleep(2)

origin = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[3]')
origin.click()
time.sleep(2)
city1 = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[3]/div/div/ul/li[4]/a')
city1.click()
logging.info('Kathamandu city was selected.')

destination = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[4]/div/button/span[1]')
destination.click()
time.sleep(1)
city2 = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[4]/div/div/ul/li[4]/a/span[1]')
city2.click()
logging.info('Janakpur was selected.')

departure= browser.find_element_by_id('from')
departure.click()
time.sleep(2)
date = browser.find_element_by_xpath('//a[text()="15"]')
date.click()

raturn = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[6]')
raturn.click()
time.sleep(2)
date2 = browser.find_element_by_xpath('//a[text()="20"]')
date2.click()



nationality = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[7]')
nationality.click()
time.sleep(2)
choose = browser.find_element_by_xpath('//span[text()="Nepal"]')
choose.click()


adults = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[8]')
adults.click()
time.sleep(2)
no_of_adults = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[8]/div/div/ul/li[3]/a')
no_of_adults.click()


child = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[9]')
child.click()
time.sleep(2)
no_of_child = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[9]/div/div/ul/li[2]/a')
no_of_child.click()
time.sleep(1)


search = browser.find_element_by_xpath('//*[@id="search-flight"]/div/div[11]')
search.click()

price = browser.find_element_by_xpath('/html/body/section[5]/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div')
price.click()
time.sleep(2)

browser.execute_script("window.scrollTo(0, 500)")

time.sleep(2)

price1 = browser.find_element_by_xpath('/html/body/section[5]/div/div[2]/div[3]/div[6]/table/tbody/tr[1]/td[4]/div/label')
price1.click()
time.sleep(2)


next = browser.find_element_by_id('continue-booking-btn')
next.click()

title = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/button/span[1]')
title.click()
time.sleep(1)
mr = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/ul/li[2]/a')
mr.click()
time.sleep(2)

fname = browser.find_element_by_id('first_name')
fname.send_keys("Subesh")
time.sleep(2)

lname = browser.find_element_by_id('last_name')
lname.send_keys("Tharu")
time.sleep(2)


gender = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[3]/div[1]/div[4]/div/div/button/span[1]')
gender.click()
male = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[3]/div[1]/div[4]/div/div/div/ul/li[2]/a')
male.click()
time.sleep(2)

nepal = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[3]/div[1]/div[5]/div/div/div/button/span[1]')
nepal.click()
country = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[3]/div[1]/div[5]/div/div/div/div/ul/li[1]/a')
country.click()
time.sleep(2)

mobile_no = browser.find_element_by_id('mobile')
mobile_no.send_keys('0900000000')
time.sleep(2)

email = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[3]/div[2]/div[2]/div/div[1]/input')
email.send_keys('subesh@gmail.com')
time.sleep(2)

passanger = browser.find_element_by_id('is_self_passenger')
passanger.click()
time.sleep(3)

browser.execute_script("window.scrollTo(0, 500)")

document_type = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[6]/div[2]/div/div[7]/div/div/button/span[1]')
document_type.click()
time.sleep(2)
select = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[6]/div[2]/div/div[7]/div/div/div/ul/li[2]/a')
select.click()
time.sleep(2)

document_number = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[6]/div[2]/div/div[8]/div/div/input')
document_number.send_keys('0001')
time.sleep(2)

terms_n_condition = browser.find_element_by_xpath('//*[@id="passengerForm"]/div[1]/div[9]/div[1]/label/input')
terms_n_condition.click()

next1 = browser.find_element_by_xpath('//*[@id="next-btn"]')
next1.click()

browser.save_screenshot('last_process_msg.png')
logging.info('Screenshot was captured.')

browser.close()
logging.info('Browser was closed successfully.')


