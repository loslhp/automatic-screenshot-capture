#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Automatic Screenshot
#pip install selenium


# In[1]:


#Script para tirar screenshot de uma pagina web
#Using selenium and chromedriver (https://chromedriver.chromium.org/downloads)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


# In[2]:


data_atual = datetime.today().strftime('%d_%m_%Y')
print (data_atual)


# In[3]:


#Opening chromedriver * check if it is the same version of chrome

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1200x600')
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(executable_path='C:/......./chromedriver.exe')
URL = 'https:yoursite'
driver.get(URL)
time.sleep(10)


# In[4]:


#where the screenshot will be stored
path = 'C:/......./screenshot/'
filename = 'name_screenshot_' + data_atual + '.png'
driver.get_screenshot_as_file(path + filename) 
driver.quit()

