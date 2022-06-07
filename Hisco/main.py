from time import sleep
from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from threading import Thread
import multiprocessing
import numpy as np
import threading
import time
threads = []
ans = []
items = []

class myThread(threading.Thread):
    def __init__(self, i, t1):
        threading.Thread.__init__(self)
        self.i = i
        self.t1 = t1

    def run(self):
        print ("from thread i = ", self.i)
        self.t1.run()
        while self.t1.check_done() != True:
            sleep(10)
            #print(self.t1.get_items())
        ans.append(self.t1.get_items())
        print(ans)


class Getter(object):
    def __init__(self, p):
        self.links = p
        self.d = webdriver.Chrome()
        self.items = []
        self.isDone = False
        #print("init: ", len(self.links))
        

    def loading_page(self,page):
        self.d.get(page)

    def fill_data(self):
        item = {}
        print(3.0)
        item['price-sale'] = self.d.find_element(by=By.CSS_SELECTOR, value=".price-sale").text
        print("3.1: ", item['price-sale'])
        try:
            item['price-old'] = self.d.find_element(by=By.CSS_SELECTOR, value=".price-old").text
        except:
            item['price-old'] = self.d.find_element(by=By.CSS_SELECTOR, value=".price-sale").text
        print ("4: ", item['price-old'])
        item['MFG#'] = self.d.find_element(by=By.CSS_SELECTOR, value=".item-num-mfg span").text
        item['Hisco#'] = self.d.find_element(by=By.CSS_SELECTOR, value=".item-num-sku span").text
        print(5)
        # substr = ''
        # for i in self.d.find_elements(by=By.CSS_SELECTOR, value=".isc-pricebreaks .col-1"):
        #     if i.text.isdigit():
        #         substr+=i.text+','
        try:
            item['Available-Qty'] = self.d.find_element(by=By.CSS_SELECTOR, value=".availability span").text
        except:
            item['Available-Qty'] = self.d.find_element(by=By.CSS_SELECTOR, value=".outstock").text
        # try:
        #     item['Available-Qty']=substr[:-1]
        # except:
        #     item['Available-Qty']= "N/A"
        print("6: ", item['Available-Qty'])
        try:
            item['Lead-Time'] = self.d.find_element(by=By.CSS_SELECTOR, value=".lead-date").text[42:]
        except:
            item['Lead-Time'] = "N/A"
        print(7)
        try:
            item['product-weight'] = self.d.find_elements(by=By.CSS_SELECTOR, value=".shipping-weight")[0].text[16:]
        except:
            item['product-weight'] = "N/A"
        print(8)
        try:
            item['Country-of-Origin'] = self.d.find_elements(by=By.CSS_SELECTOR, value=".shipping-weight")[1].text[19:]
        except:
            item['Country-of-Origin'] ="N/A"
        print('++++++++++++')
        print(item)
        print('++++++++++++')
        print(9)
        return item
        
    def run(self):
        print (1)
        for i in self.links:
                try:
                    print('**************************')
                    print(i)
                    self.loading_page(i)
                    print(2)
                    sleep(10)
                    #WebDriverWait(self.d, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shipping-weight")))
                    #WebDriverWait(self.d, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".price-sale")))
                    #WebDriverWait(self.d, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".isc-pricebreaks .col-1")))
                    print(3)
                    tmp = self.fill_data()
                    print(10)
                    self.items.append(tmp)
                except:
                    print("ERORR at: ", i)
        self.isDone = True
        self.d.quit() 
        

    def check_done(self):
        return self.isDone   
    def get_items(self):
        return self.items 


def write_to_csv(items):
    header = ['price-sale', 'price-old', 'MFG#', 'Hisco#', 'Available-Qty', 'Lead-Time', 'product-weight', 'Country-of-Origin']
    with open('output.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(items)

def get_list_product():
    f = open("Hisco.txt",'r',encoding = 'utf-8')
    return f.readlines()

def read_all_products():
    firstLink = 'https://www.hisco.com/Product/'
    products_id = get_list_product()
    products = []
    for product in products_id:
        next_page = firstLink + product
        next_page.replace('\n','')
        products.append(next_page)
    print(products[0])
    return products

# def threaded_function(t1, i):
#     t1.run()
#     while t1.check_done() != True:
#        sleep(10)
#        print(t1.get_items())
#     ans.append(t1.get_items())
#     print(ans)


def main():
    
    products = read_all_products()
    num_threads = 10
    split = np.array_split(products, num_threads)
    #print(len(split[0].tolist()))
    threads = []
    for i in range(num_threads):
        print(len(split[i].tolist()))
        t = Getter(split[i].tolist())
        thread = myThread(i,t)

        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    write_to_csv(ans)


if __name__ == "__main__":
    main()