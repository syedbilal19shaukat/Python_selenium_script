import sys, os, time
import urllib.request
import getpass
import py2exe
import requests
import openpyxl
import time
from random import *
import random,string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
CSV_path1 = input("Please enter location to save file: ")
CSV_path =  CSV_path1.replace('/','//')
data = []
if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/search?hl=en&tbm=lcl&sxsrf=ALeKk008F5V0kr0zsRMgNHS5I5GU1kBBLg%3A1594412492728&ei=zM0IX_aHLOaPlwSzhYuQCQ&q=consultant&oq=consultant&gs_l=psy-ab.3...0.0.0.413342.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.rI9m1z71fHU')   
for i in range(1, 10):
         j=1
         imagename=[]
         skuu=[] 
         for link1 in range(1, 5):
             time.sleep(6)
             link = driver.find_element_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div[%d]' % (j,)).click()
             link2 = driver.current_url
             print(link2)
             Image = dict()
             sampleImage = dict()
             fullname = dict()
             filepath = dict()
             time.sleep(2)
             try:
                 title = driver.find_element_by_xpath('//*[@id="akp_tsuid4"]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div/div[@data-attrid="title"]/span | //async-local-kp/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div/div[@data-attrid="title"]/span').text
                 print(title)
             except:
                    title = 'No Title'
                    print(title)
             time.sleep(2)
             try:
                 address = driver.find_element_by_xpath('//*[@id="akp_tsuid4"]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/span[2] | //div[@data-attrid="kc:/location/location:address"]/div/div/span[2]').text
                 print(address)
             except:
                    address = 'No address'
                    print(address)
             time.sleep(2)       
             try:
                 phone_no = driver.find_element_by_xpath('//*[@id="akp_tsuid4"]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[@data-attrid="kc:/collection/knowledge_panels/has_phone:phone"]/div/div//following::span[1]/a/span | //async-local-kp/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[@data-attrid="kc:/collection/knowledge_panels/has_phone:phone"]/div/div//following::span[1]/a/span | //div[@data-attrid="kc:/collection/knowledge_panels/has_phone:phone"]/div/div//following::span[1]/span/span').text
                 print(phone_no)
             except:
                    phone_no = 'No phone'
                    print(phone_no)
             time.sleep(2)   
             j=j+1
             data.append((link2,title,address,phone_no))
             import pandas as pd
             df = pd.DataFrame(data,columns =['url','title','address','phone_no'])
             df.to_csv(CSV_path+'//file.csv',index=False,encoding='utf-8')
         pagination_click = driver.find_element_by_xpath('//*[@id="rl_ist0"]/div[2]/div/table/tbody/tr/td[@class="b d6cvqb"]/a[@id="pnnext"]').click()
         time.sleep(5)
