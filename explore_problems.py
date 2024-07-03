import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Define the ChromeDriver service
s = Service('chromedriver.exe')

# Initialize the WebDriver with the service 
driver = webdriver.Chrome(service=s)

heading_class=".text-title-large.font-semibold.text-text-primary.dark\\:text-text-primary"  # for heading of the problem
body_class=".elfjS"           #for the description of the problem
index = 1             #counter variable for folders inside Qdata folder 
QDATA_FOLDER="Qdata"  # directory where the data will be saved

def get_array_of_links():
    arr=[] #array to store the lines of file
    with open('leetcode.txt','r') as file:  # read each line one by one        
        for line in file:  #processing the line from the file
            arr.append(line) #performing append on every line to add them to array
    return arr 

def add_text_to_index_file(text):
    index_file_path=os.path.join(QDATA_FOLDER,"index.txt") #this gives a path to Qdata folder's index.txt
    with open(index_file_path,'a') as index_file:          # opens index.txt as index_file using the path
        index_file.write(text+"\n")                        # writes the headings of every problem in the index_file one after the other (because of "\n")

def add_text_to_Qindex_file(text):
    index_file_path=os.path.join(QDATA_FOLDER,"Qindex.txt")  #this gives a path to Qdata folder's Qindex.txt
    with open(index_file_path,'a') as Qindex_file:           # opens Qindex.txt as Qindex_file using the path
        Qindex_file.write(text)                              # writes in to the Qindex_file

def create_and_add_text_to_file(file_name,text):
    folder_path=os.path.join(QDATA_FOLDER,file_name)
    os.makedirs(folder_path,exist_ok=True)
    file_path=os.path.join(folder_path,file_name+".txt")
    with open(file_path,'w') as new_file:
        new_file.write(text)


def getPageData(url,index):
    try:
        driver.get(url)
        WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,body_class)))
        time.sleep(1)
        heading=driver.find_element(By.CSS_SELECTOR,heading_class)
        body=driver.find_element(By.CSS_SELECTOR,body_class)
        print(heading.text)
        if (heading.text):
            add_text_to_index_file(heading.text)
            add_text_to_Qindex_file(url)
            create_and_add_text_to_file(str(index),body.text)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False
    
arr=get_array_of_links()
for link in arr:
    success=getPageData(link,index)
    if (success):
        index=index+1
driver.quit()