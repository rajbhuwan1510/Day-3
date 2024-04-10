from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g")
soup=BeautifulSoup(driver.page_source,'html.parser')

#class names at flipkart website check accoring to your browser setting it may be different 
names = "_4rR01T"
prices = "_30jeq3 _1_WHN1"
rating = "_3LWZlK"

user_input=input("Enter the names of device you want to scrap from flipkart") # getting input for the search item in flipkart
driver = webdriver.Chrome()
names = "_4rR01T"
userinput_names=[]
#loop for scrapping data from page 1 to 11
for i in range(1,11):
    driver.get(f"https://www.flipkart.com/search?q={user_input}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    time.sleep(5)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    userinput_names_div=soup.find_all(class_=names)
    for j in userinput_names_div:
        print(j.text)
        userinput_names.append(j.text)
        
#close the browser        
driver.quit()

#if you want to print the data
print(userinput_names)
