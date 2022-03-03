from turtle import position
from unicodedata import digit
from selenium import webdriver
import random
import time


web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdXU16-V9Gypiqy4OYF6p3WsYgs8pk1ZzDx7J8bm9HSi_3rTA/viewform')
i =1
for x in range(250):

    time.sleep(3)

    Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    Next.click()
    
    time.sleep(2)
    Gender = [ web.find_element_by_xpath('//*[@id="i5"]/div[3]/div'), 
               web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')]
    a=random.randint(0,1)
    Gender[a].click()

    Age = [ web.find_element_by_xpath('//*[@id="i21"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i24"]/div[3]/div')]
    b=random.randint(0,1)
    Age[b].click()
    time.sleep(1)

    Edu = [ web.find_element_by_xpath('//*[@id="i37"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i40"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i43"]/div[3]/div')]
    b=random.randint(0,2)
    Edu[b].click()
    time.sleep(1)

    Race = [web.find_element_by_xpath('//*[@id="i53"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i56"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i59"]/div[3]/div'),]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    income = [  web.find_element_by_xpath('//*[@id="i72"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i75"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i78"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i69"]/div[3]/div')]
    b=random.randint(0,3)
    income[b].click()
    time.sleep(1)

    yes = [ web.find_element_by_xpath('//*[@id="i91"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i94"]/div[3]/div'),]
    b=random.randint(0,1)
    yes[b].click()
    time.sleep(1)

    # income = [  web.find_element_by_xpath('//*[@id="i104"]/div[3]/div'),
    #             web.find_element_by_xpath('//*[@id="i107"]/div[3]/div'),
    #             web.find_element_by_xpath('//*[@id="i110"]/div[3]/div'),
    #             web.find_element_by_xpath('//*[@id="i113"]/div[3]/div')]
    # a=random.randint(0,1)
    # b=random.randint(2,3)
    # income[b].click()
    # time.sleep(1)
    # income[a].click()
    # time.sleep(1)
    # c = web.find_element_by_xpath('//*[@id="i101"]/div[3]/div')
    # c.click()
    income = [  web.find_element_by_xpath('//*[@id="i101"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i104"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i107"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i110"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i113"]/div[3]/div')]
    a=random.randint(0,4)
    income[a].click()
    time.sleep(1)
   
    yes = [ web.find_element_by_xpath('//*[@id="i123"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i126"]/div[3]/div'),]
    b=random.randint(0,1)
    yes[b].click()
    time.sleep(1)

    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()
    ###first page #####

    time.sleep(2)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    # CustomerService
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    # convenience
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    # Qualityofservice
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
#trust
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()
#thirdPage
    time.sleep(2)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    Organization = [web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)

    another = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()

    print(f"Done: {i}")
    i+=1