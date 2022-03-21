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

groups_id = ['1608400319378074'] #,'425147792032823','668413097194404']
token = "EAABwzLixnjYBAASqQbaTXCeZAZCqGnCBUuwnZBtZAsi5x2M0RAQJrIZC4yxlOSPZA7GVdU52xcLW33CgrrUv3y014OOA5zahIcZCPRgY9MgNj4GbOhs44CGjN3StbmwdeynKEhzroZA1OF62xgpZBHfD4lC5cYMJz6rYsLZCMLsrU0f5Yw8ViF1uJd"
message = "https://www.facebook.com/camera24hanoi/ chuyên lắp đặt camera, thiết bị thông minh. Liên hệ 0789753999. Chi tiết có tại hptcamera.com.vn"
 
def threaded_function(post_id, mess):
    print(post_id)
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.facebook.com')
    email_element = driver.find_element_by_css_selector('input[name="email"]')
    email_element.send_keys("0989996815")
    pass_element = driver.find_element_by_css_selector('input[name="pass"]')
    pass_element.send_keys("Kh0ngbiet")
    driver.find_element_by_css_selector('button[name="login"]').click()
    time.sleep(8)
   
    driver.get('https://www.facebook.com/{}'.format(post_id))
    time.sleep(4)
    box_comment = driver.find_element_by_css_selector('div[role="textbox"]')
    box_comment.send_keys(mess)
    box_comment.send_keys(Keys.ENTER)
    time.sleep(8)
  
    sleep(1)
        
class Group(object):
    last_post_time = ''
    id_latest_post = ''
    mess_to_post = 'Lien he: htpcamera, cam ket re nhat thi truong'
    def __init__(self, group_id, graph):
        self.group_id = group_id
        self.graph = graph
        
    def is_updated_post(self):
        tmp_lastest_time = self.graph.get_object(self.group_id, fields='updated_time')
        tmp_lastest_post = self.graph.get_object(self.group_id, fields='feed.limit(1)')['feed']['data'][0]['id']
       
        if tmp_lastest_post == self.id_latest_post:
            return False
        self.id_latest_post = tmp_lastest_post
        return True

    def get_lastest_post(self):
        return self.id_latest_post

def main():
    graph = facebook.GraphAPI(token)
    graphs_list = []
    
    for group in groups_id:
        graphs_list.append(Group(group,graph))
    while(True):
        for gr in graphs_list:
            if gr.is_updated_post():
                print ("FOUND UPDATE!!!!!")
                post_id = gr.get_lastest_post()
                #create new thread to post
                thread = Thread(target = threaded_function, args = (post_id,message ))
                thread.start()
                thread.join()
        sleep (60)
if __name__ == "__main__":
    main()
