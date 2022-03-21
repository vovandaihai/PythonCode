# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import facebook
from threading import Thread
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

groups_id = ['1259652814384252']
token = "EAABwzLixnjYBABRrYd4U0cvZCeeZA2fI3gTn4X9ISvmwCzxK0wJ2UdnBW2kRkLUuPQZAbiFZCu3NoSXPoTPOplPZB6AZArP5KiL3DU4nsCxPjDyZCiIxga9kHJUWN0W2kMg343bdutoqMVMjc2Vm4v7kZCQvDqMVkNv8a5LUehdTebmGh0StPZAwl"
message = "Liên hệ HTP camera lắp đặt trọn gói camera giá rẻ nhất thị trường"
 
def threaded_function(post_id, mess):
    print(post_id)
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.facebook.com')
    email_element = driver.find_element_by_css_selector('input[name="email"]')
    email_element.send_keys("kaisoul.yk")
    pass_element = driver.find_element_by_css_selector('input[name="pass"]')
    pass_element.send_keys("VoHai123")
    driver.find_element_by_css_selector('button[name="login"]').click()
    time.sleep(8)
   
    driver.get('https://www.facebook.com/{}'.format(post_id))
    time.sleep(4)
    box_comment = driver.find_element_by_css_selector('div[role="textbox"]')
    box_comment.send_keys(mess)
    #box_comment.send_keys(Keys.ENTER)
    time.sleep(8)
  
    sleep(1)
        
class Group(object):
    group_id = ''
    last_post_time = ''
    graph = ''
    mess_to_post = 'Lien he: htpcamera, cam ket re nhat thi truong'
    def __init__(self, group_id, graph):
        self.group_id = group_id
        self.graph = graph
        
    def is_updated_post(self):
        tmp_lastest = self.graph.get_object(self.group_id, fields='updated_time')
        if tmp_lastest == self.last_post_time:
            return False
        
        self.last_post_time = tmp_lastest
        return True
    def get_time_update(self):
        return self.last_post_time
    def get_lastest_post(self):
        tmp_lastest = self.graph.get_object(self.group_id, fields='feed.limit(1)')
        id_latest_post = tmp_lastest['feed']['data'][0]['id']
        return id_latest_post

def main():
    graph = facebook.GraphAPI(token)
    gr = Group(groups_id[0],graph)
    
    if gr.is_updated_post():
        print(gr.get_time_update())
        post_id = gr.get_lastest_post()
        #create new thread to post
        thread = Thread(target = threaded_function, args = (post_id,message ))
        thread.start()
        thread.join()
if __name__ == "__main__":
    main()
