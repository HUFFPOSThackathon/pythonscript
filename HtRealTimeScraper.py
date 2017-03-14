import os
import sys
from pyvirtualdisplay import Display
from selenium import webdriver as wb
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
############################ A Dictionary For Matching statecodes #############
statecodes={
	'1':'goa',
	'2':'up',
	'3':'uttarakhand',
	'4':'manipur',
	'5':'punjab',
}
###################### Function for creating a custom webdriver #############
def create_ch_driver():
  chrome_options = wb.ChromeOptions()
  chrome_options.add_argument("--no-sandbox")
  return wb.Chrome("/Users/nipunarora/Desktop/django/webscraper&djangostart/seleniumscraper/chromedriver", chrome_options=chrome_options)

def getConstituencyFromPlaceName(state_code,place_name):
	####################### Create a Virtual Display for a VPS #######################
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver=create_ch_driver()
	global statecodes
	driver.get('http://www.hindustantimes.com/interactives/election-candidates-2017/%s/'%(statecodes[state_code]))
	######################## Send the name of the area you want to search for ###############################
	driver.find_element_by_id('search').send_keys(place_name)
	driver.find_element_by_id('search').send_keys(Keys.RETURN)
	################## Wait for the page to load and give you the name of the constituency #####################################
	time.sleep(1)
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="status" and text() != ""]')))
	constituency_block=driver.find_element_by_id('status')
	soup=bs(constituency_block.get_attribute("innerHTML"),"html.parser")
	#################### ADD A BUSY WAIT FOR THE AJAX TO LOAD ######################
	while not(len(soup.find_all('b'))):
		constituency_block=driver.find_element_by_id('status')
		soup=bs(constituency_block.get_attribute("innerHTML"),"html.parser")
		pass
	##########################################
	constituency_name=soup.find_all('b')[1].text
	print constituency_name
	driver.quit()

######################### Function Call Taking the arguement from the command line  #####################################
getConstituencyFromPlaceName(sys.argv[1],sys.argv[2])