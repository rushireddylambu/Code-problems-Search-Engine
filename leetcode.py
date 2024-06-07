from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Define the ChromeDriver service
s = Service('chromedriver.exe')

# Initialize the WebDriver with the service 
driver = webdriver.Chrome(service=s)

#URL for the pages to scrape
page_url="https://leetcode.com/problemset/?page="

driver.get(page_url)