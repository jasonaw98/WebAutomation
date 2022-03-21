from selenium import webdriver
import random
import time


web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSd8RFhpt6IDM50hk2Oq8JY7az-S-Uc9Yfpqc18LZT5QgA_Inw/viewform?vc=0&c=0&w=1&flr=0')
i =1
for x in range(100):

    time.sleep(3)
    
    time.sleep(2)
    Gender = [ web.find_element_by_xpath('//*[@id="i5"]/div[3]/div'), 
               web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')]
    a=random.randint(0,1)
    Gender[a].click()

    Age = [ web.find_element_by_xpath(f'//*[@id="i15"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i18"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i21"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i24"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i27"]/div[3]/div')]
    b=random.randint(0,4)
    Age[1].click()
    time.sleep(1)

    Edu = [ web.find_element_by_xpath('//*[@id="i34"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i37"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i40"]/div[3]/div'),]
    b=random.randint(0,2)
    Edu[b].click()
    time.sleep(1)

    Race = [web.find_element_by_xpath('//*[@id="i50"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i53"]/div[3]/div'),]
    b=random.randint(0,1)
    Race[b].click()
    time.sleep(1)

    income = [  web.find_element_by_xpath('//*[@id="i63"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i66"]/div[3]/div'),]
    b=random.randint(0,1)
    income[b].click()
    time.sleep(1)


    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()
    ###first page #####

    time.sleep(2)
    z=2
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

   
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)
    z=2
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    
    another = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    another.click()

    time.sleep(2)
    z=2
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    another = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    another.click()

    time.sleep(2)
    z=2
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    another = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    another.click()

    time.sleep(2)
    z=2
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    another = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    another.click()

    time.sleep(2)
    another = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()
    print(f"Done: {i}")
    i+=1