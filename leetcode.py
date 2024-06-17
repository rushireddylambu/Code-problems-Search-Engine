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
# time.sleep(7)

def get_a_tags(url):
    driver.get(url)
    time.sleep(7)
    links=driver.find_elements(By.TAG_NAME,"a")          #an 'a' tag looks like this "<a href="https://www.w3schools.com">Visit W3Schools.com!</a>""
    print(links)                                          #gives all the 'a tag' web elements 
    http_links=[]
    pattern="/problems"
    for i in links:
        try:
            if pattern in i.get_attribute("href"):        #getting the attribute href gets the http links
                http_links.append(i.get_attribute("href"))  # then i added the links to hhtp_links
        except:
            pass
    http_links=list(set(http_links))       #removed the repeated ones
    return http_links 

my_http_links=[]                       #to collect all the links in the 64 pages i created a list
for i in range(1,65):
    my_http_links+=(get_a_tags(page_url+str(i)))   #call the get_a_tags function so it scraps the links of all the problems 
                                                   # in every page out of 64 and adds it to the list my_http_links
my_http_links=list(set(my_http_links)) # removing the duplicate ones

#opening a txt file to store all the problem links 
with open('leetcode.txt','a') as f:        
    for j in my_http_links:
        f.write(j+'\n')     # writing the links in a txt file one after the another using '\n'
print(len(my_http_links))   # printing the total number of problem links
driver.quit()
