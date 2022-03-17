from selenium import webdriver
import random
import time


web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdVArBP63Xx0kHMItTXfYrmLSt-Q0bTzOviLI1MPAbKO6tlIg/viewform')
i =1
for x in range(250):

    time.sleep(3)
    
    time.sleep(2)
    Gender = [ web.find_element_by_xpath('//*[@id="i7"]/div[3]/div'), 
               web.find_element_by_xpath('//*[@id="i10"]/div[3]/div')]
    a=random.randint(0,1)
    Gender[a].click()

    h=17
    Age = [ web.find_element_by_xpath(f'//*[@id="i{h}"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i{h+3}"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i23"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i26"]/div[3]/div'),
            web.find_element_by_xpath(f'//*[@id="i29"]/div[3]/div')]
    b=random.randint(0,4)
    Age[1].click()
    time.sleep(1)

    Edu = [ web.find_element_by_xpath('//*[@id="i36"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i39"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i42"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i45"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i48"]/div[3]/div')]
    b=random.randint(0,4)
    Edu[b].click()
    time.sleep(1)

    Race = [web.find_element_by_xpath('//*[@id="i55"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i58"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i61"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i64"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i67"]/div[3]/div'),]
    b=random.randint(0,4)
    Race[b].click()
    time.sleep(1)

    income = [  web.find_element_by_xpath('//*[@id="i74"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i77"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i80"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i83"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i86"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i89"]/div[3]/div')]
    b=random.randint(0,5)
    income[b].click()
    time.sleep(1)

    yes = [ web.find_element_by_xpath('//*[@id="i99"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i102"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i105"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i108"]/div[3]/div'),]
    b=random.randint(0,3)
    yes[b].click()
    time.sleep(1)

    yes = [ web.find_element_by_xpath('//*[@id="i115"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i118"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i121"]/div[3]/div'),]
    b=random.randint(0,2)
    yes[b].click()
    time.sleep(1)

    yes = [ web.find_element_by_xpath('//*[@id="i128"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i131"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i134"]/div[3]/div'),]
    b=random.randint(0,2)
    yes[b].click()
    time.sleep(1)

    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()
    ###first page #####

    time.sleep(2)
    z=4
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
   
    z=10
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)

    z=16
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
   
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)
    z=4
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    b=random.randint(0,4)
    Organization[b].click()
    time.sleep(1)
    z+=1
    Organization = [web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
                    web.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{z}]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'),]
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