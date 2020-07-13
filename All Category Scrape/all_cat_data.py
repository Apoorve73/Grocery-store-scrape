import urllib.request
import time
import random as r
from selenium import webdriver
import json
import pprint

data = {}
data['image_url']= list()
allcat = data['image_url']

driver = webdriver.Chrome("<PATH OF CHROMEDRIVER>")

driver.get('https://www.jiomart.com/all-category')
time.sleep(5)
# get the image source


img_class = driver.find_elements_by_class_name('cat-img')
title_class = driver.find_elements_by_class_name("clsgetname")

num = 0
for i in img_class:
    src = i.find_elements_by_tag_name('img')
    link = src[0].get_attribute('src')
    #print(link)

    title = title_class[num].text
    allcat.append({
        title : link
    })
    # if num == 2:
    #     find = driver.find_element_by_xpath('//*[@id="shop_by_cat"]/div/div[3]')
    #     find.click()
    #     time.sleep(1)
    #     find.click()
    #     time.sleep(1)
    # allcat.append({
    #     title : link
    # })
    #download the image
    #urllib.request.urlretrieve(link, str(num)+".png")
    num+=1
#
with open("data.txt", "w") as f:
    json.dump(data, f)
    pprint.pprint(data)

driver.close()