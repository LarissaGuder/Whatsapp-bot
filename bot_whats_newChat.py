# -*- coding: utf-8 -*-
'''
Created on Jul 6, 2016

@author: indrajit.n
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox()



driver = webdriver.Chrome()
driver.get("http://web.whatsapp.com/")

time.sleep(25)

newChat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/button')
newChat.click()
find = driver.find_element_by_xpath('//input[@title="Search contacts"]')
find.send_keys('Contact name')
time.sleep(3)
elem = driver.find_element_by_xpath('//span[contains(text(),"Contact name")]')
elem.click()
time.sleep(5)
elem1 = driver.find_element_by_xpath('//div[@class="pluggable-input-body copyable-text selectable-text"]')
i = 1
while True:
    elem1.send_keys('pruuuuu+ ' + str(i))
    i = i + 1
    driver.find_element_by_class_name('compose-btn-send').click()
