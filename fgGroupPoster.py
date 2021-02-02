# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class fgGroupPoster(object):
    mess = 'Chia sẻ thành công mời nhập link bài khác'

    def __init__(self, account, password, groups_links_list):
        print ("haivvd:", account, password, groups_links_list)

        #const selector
        shareBtn_0like = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80 > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.d2edcug0.oh7imozk.tr9rh885.abvwweq7.ejjq64ki > div > div > div > div > div > div > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.hybvsw6c.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs.k4urcfbm.sbcfpzgs > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div > div > div:nth-child(3) > div"
        shareBtn_xlike = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80 > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.d2edcug0.oh7imozk.tr9rh885.abvwweq7.ejjq64ki > div > div > div > div > div > div > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.hybvsw6c.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs.k4urcfbm.sbcfpzgs > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div.ozuftl9m.tvfksri0 > div > div:nth-child(3) > div"
        buttonTuychonkhacVideo = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div.rq0escxv.jgsskzai.cwj9ozl2.nwpbqux9.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn.k4urcfbm > div > div:nth-child(4) > div"
        buttonNumber7 = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div.rq0escxv.jgsskzai.cwj9ozl2.nwpbqux9.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn.k4urcfbm > div > div:nth-child(7) > div"
        buttonChiasenhomVideo = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div.rq0escxv.jgsskzai.cwj9ozl2.nwpbqux9.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn.k4urcfbm > div > div.sj5x9vvc > div:nth-child(3) > div"
        buttonChiasenhomImage = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div.rq0escxv.jgsskzai.cwj9ozl2.nwpbqux9.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn.k4urcfbm > div > div:nth-child(4) > div"
        buttonChiasenhomImage5 = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div.rq0escxv.jgsskzai.cwj9ozl2.nwpbqux9.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn.k4urcfbm > div > div:nth-child(5) > div"
        buttonChiasenhomImage6 = "#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div.rq0escxv.jgsskzai.cwj9ozl2.nwpbqux9.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn.k4urcfbm > div > div:nth-child(6) > div"
        sharemsg = "#mount_0_0 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div.tr9rh885 > div.gh1tjcio.dhix69tm.wkznzc2l.oud54xpy.j83agx80 > div.dhix69tm.buofh1pr.o8rfisnq > span > div > div > div._5rpb > div"
        #timtheonhom = "#mount_0_0 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div.tr9rh885 > div:nth-child(3) > div > div.n851cfcs.wkznzc2l.dhix69tm.n1l5q3vz > div > div > label > input"
        timtheonhom = "#mount_0_0 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn > div.glvd648r > div > div > div.n851cfcs.wkznzc2l.dhix69tm.n1l5q3vz > div > div > label > input"
        postBtn = "#mount_0_0 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn > form > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn > div > div > div.j83agx80.cbu4d94t.f0kvp8a6.mfofr4af.l9j0dhe7.oh7imozk > div.ihqw7lf3.discj3wi.l9j0dhe7 > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.hv4rvrfc.dati1w0a.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg > div > div"
    # Set up text content to post
        message = '''
Mua đồ xinh, lại còn có quà tặng mang về các chị yêu ơi

https://www.facebook.com/Thoitrangphukienmaimai/posts/112112284125813'''


    # Login Facebook
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome('D:\Program Files\chromedriver_win32\chromedriver.exe', options=chrome_options)
        driver.get('https://www.facebook.com')
        emailelement = driver.find_element(By.XPATH,'//*[@id="email"]')
        emailelement.send_keys(account)
        passelement = driver.find_element(By.XPATH,'//*[@id="pass"]')
        passelement.send_keys(password)
        loginelement = driver.find_element(By.XPATH,'//*[@id="u_0_b"]')
        loginelement.click()
        time.sleep(8)
    # Post on each group
        for group in groups_links_list:
            ret = driver.get(group)
            time.sleep(5)
            i = 1
        #click nut share
            while True:
                try:
                    driver.find_element_by_css_selector(shareBtn_0like).click()
                except:
                    driver.find_element_by_css_selector(shareBtn_xlike).click()
                time.sleep(2)
        
                try:
                    check = driver.find_element_by_css_selector(buttonNumber7)
                except:
                    check = None
                if (check != None): #video
                    try:
                        driver.find_element_by_css_selector(buttonTuychonkhacVideo).click()
                        time.sleep(1)
                    except:
                        mess = "Khong bam dc vao tuy chon khac!"
                        print("Khong bam dc vao tuy chon khac!")
				    
                    try:
                        driver.find_element_by_css_selector(buttonChiasenhomVideo).click()
                        time.sleep(1)
                    except:
                        mess = "Khong bam dc chia se nhom (video case)!"
                        print("Khong bam dc chia se nhom (video case)!")
                else: #image
                    try:
                        check2 = driver.find_element_by_css_selector(buttonChiasenhomImage6)
                    except:
                        check2 = None
                    if (check2 != None):
                        try:
                            driver.find_element_by_css_selector(buttonChiasenhomImage5).click()
                            time.sleep(2)
                        except:
                            mess = "Khong bam dc chia se nhom (image case)!"
                            print("Khong bam dc chia se nhom (image case)!")
                    else:
                        try:
                            driver.find_element_by_css_selector(buttonChiasenhomImage).click()
                            time.sleep(2)
                        except:
                            mess = "Khong bam dc chia se nhom (image case)!"
                            print("Khong bam dc chia se nhom (image case)!")
                try:
                    timtheonhombtn = driver.find_element_by_css_selector(timtheonhom)
                    timtheonhombtn.send_keys("chợ")
                    time.sleep(4)
                except:
                    mess = "Khong tim thay filter group!"
                    print("Khong tim thay filter group!")
        

                try:
                    link1 = driver.find_element_by_css_selector("#mount_0_0 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn > div.glvd648r > div > div > div:nth-child(2) > div > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div > div > div > div:nth-child(2) > div > div:nth-child("+str(i)+") > div").click()
                    i = i + 1
                    time.sleep(3)
                except:
                    print ('khong click vao link' + str(i) + ' dc')
                    mess ='khong click vao link' + str(i)
                    break
                try:
                    post = driver.find_element_by_css_selector(postBtn).click()
                    time.sleep(3)    
                except:
                    print ('khong bam dc share link' + str(i))
                    mess ='khong bam dc share link' + str(i)
        driver.quit()

#fgGroupPoster = fgGroupPoster("van.hai.7186","abc13579",["https://www.facebook.com/Thoitrangphukienmaimai/posts/119855336684841", ])


