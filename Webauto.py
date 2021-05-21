from selenium import webdriver
import random
import time


web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSd0wor-OXeGPmb5e-vRULmD-WnQwj15aIpVfqP-mkt7RtnZgw/viewform?usp=sf_link')
for x in range(30):

    time.sleep(3)

    Gender = [ web.find_element_by_xpath('//*[@id="i8"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')]
    a=random.randint(0,1)
    Gender[a].click()
    time.sleep(1)
    Age = [ web.find_element_by_xpath('//*[@id="i17"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i23"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i20"]/div[3]/div'),web.find_element_by_xpath('//*[@id="i26"]/div[3]/div')]
    b=random.randint(0,3)
    Age[b].click()
    time.sleep(1)
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span/span')
    submit.click()
    ###first page #####

    time.sleep(2)
    Gender = [ web.find_element_by_xpath('//*[@id="i5"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')]
    t=random.randint(0,1)
    Gender[t].click()
    time.sleep(1)
    Gender1 = [ web.find_element_by_xpath('//*[@id="i15"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i18"]/div[3]/div')]
    t=random.randint(0,1)
    Gender1[t].click()
    time.sleep(1)
    Gender2 = [ web.find_element_by_xpath('//*[@id="i25"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i28"]/div[3]/div')]
    a=random.randint(0,1)
    Gender2[a].click()
    time.sleep(1)
    Gender3 = [ web.find_element_by_xpath('//*[@id="i35"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i38"]/div[3]/div')]
    a=random.randint(0,1)
    Gender3[a].click()
    time.sleep(1)
    Gender4 = [ web.find_element_by_xpath('//*[@id="i45"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i48"]/div[3]/div')]
    a=random.randint(0,1)
    Gender4[a].click()
    time.sleep(1)
    Gender5 = [ web.find_element_by_xpath('//*[@id="i55"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i58"]/div[3]/div')]
    a=random.randint(0,1)
    Gender5[a].click()
    time.sleep(1)
    Gender6 = [ web.find_element_by_xpath('//*[@id="i65"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i68"]/div[3]/div')]
    a=random.randint(0,1)
    Gender6[a].click()
    time.sleep(1)
    Gender7 = [ web.find_element_by_xpath('//*[@id="i75"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i78"]/div[3]/div')]
    a=random.randint(0,1)
    Gender7[a].click()
    time.sleep(1)
    Gender8 = [ web.find_element_by_xpath('//*[@id="i85"]/div[3]/div'), web.find_element_by_xpath('//*[@id="i88"]/div[3]/div')]
    a=random.randint(0,1)
    Gender8[a].click()
    time.sleep(1)
    NextPage = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span/span')
    NextPage.click()
    # #secondPage

    #Third page
    time.sleep(2)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()

    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div'),
            ]
    c=random.randint(0,3)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()

    time.sleep(1)
    NExt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span/span')
    NExt.click()
    #Third page

    #final page
    time.sleep(2)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[3]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[4]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[5]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[6]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[7]/div/div/div[3]/div'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)

    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span/span')
    submit.click()

    time.sleep(2)
    New = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    New.click()
