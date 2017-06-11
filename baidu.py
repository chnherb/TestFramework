# coding=utf-8
from selenium import webdriver
#import os

#firefoxBin = os.path.abspath(r"C:\profession\Mozilla Firefox\firefox.exe")
#os.environ["webdriver.firefox.bin"] = firefoxBin
    
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()

#driver.quit()
