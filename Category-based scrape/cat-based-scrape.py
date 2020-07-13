import urllib.request
import time
import random as r
from selenium import webdriver
import json
import pprint

data = {}
data['product_detail']= list()



def class_finding(driver):
    class_name = driver.find_elements_by_class_name('catitem')
    time.sleep(1)

    return class_name

driver = webdriver.Chrome("<PATH OF CHROMEDRIVER>")

driver.get('https://www.jiomart.com/all-category')
time.sleep(5)

class_name = class_finding(driver)

length = len(class_name)
print("Total Links: {}".format(length))

for i in range(length):
    print("Link number: {}".format(i))

    link = class_name[i].find_elements_by_tag_name('a')[0].get_attribute('href')
    #print(link)
    driver.get(link)
    time.sleep(2)

    des_class = driver.find_elements_by_class_name('category_name')
    img_class = driver.find_elements_by_class_name('cat-img')
    price_class = driver.find_elements_by_class_name('price-box')
    print(len(price_class))

    for j in range(len(price_class)//2):

        description = des_class[j].get_attribute('title')
        url = img_class[j].find_element_by_tag_name('img').get_attribute('src')
        price = price_class[j].find_element_by_id('final_price').text

        data['product_detail'].append({
            'Title': description,
            'ImageURL' : url,
            'Price' : price
        })
        #print("Description: {} \n URL: {} \n Price: {}".format(description,url,price))

    driver.get('https://www.jiomart.com/all-category')
    time.sleep(2)
    class_name = driver.find_elements_by_class_name('catitem')
    time.sleep(1)

with open('product_detail_test.txt', 'w') as outfile:
    json.dump(data, outfile)

driver.close()