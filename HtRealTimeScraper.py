import os
from pyvirtualdisplay import Display
from selenium import webdriver as wb
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
###################### Function for creating a custom webdriver #############
def create_ch_driver():
  chrome_options = wb.ChromeOptions()
  chrome_options.add_argument("--no-sandbox")
  return wb.Chrome("/Users/nipunarora/Desktop/django/webscraper&djangostart/seleniumscraper/chromedriver", chrome_options=chrome_options)
####################### Create a Virtual Display for a VPS #######################
display = Display(visible=0, size=(800, 600))
display.start()
driver=create_ch_driver()
driver.get('http://www.hindustantimes.com/interactives/election-candidates-2017/goa/')
######################## Send the name of the area you want to search for ###############################
driver.find_element_by_id('search').send_keys("ponda")
driver.find_element_by_id('search').send_keys(Keys.RETURN)
################## Wait for the page to load and give you the name of the constituency #####################################
time.sleep(1)
page_state = driver.execute_script('return document.readyState;') 
WebDriverWait(driver, 10).until(page_state=="Complete")
constituency_block=driver.find_element_by_id('status')
print constituency_block.get_attribute("innerHTML")
#soup=bs()