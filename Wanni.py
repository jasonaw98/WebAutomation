from turtle import position
from unicodedata import digit
from selenium import webdriver
import random
import time


web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSe1ASWjZDoWGchCY5low4lg0MCMO5daarAzewW9Q_UayNnWQA/viewform')
for x in range(150):

    time.sleep(3)

    Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    Next.click()
    
    time.sleep(2)
    Gender = [ web.find_element_by_xpath('//*[@id="i5"]/div[3]/div'), 
               web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')]
    a=random.randint(0,1)
    Gender[a].click()

    Age = [ web.find_element_by_xpath('//*[@id="i15"]/div[3]/div'), 
            web.find_element_by_xpath('//*[@id="i18"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i21"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i27"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i24"]/div[3]/div')]
    b=random.randint(0,4)
    Age[b].click()
    time.sleep(1)

    Race = [ web.find_element_by_xpath('//*[@id="i34"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i37"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i40"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i43"]/div[3]/div')]
    b=random.randint(0,3)
    Race[b].click()
    time.sleep(1)

    Edu = [ web.find_element_by_xpath('//*[@id="i50"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i53"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i56"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i59"]/div[3]/div'),
            web.find_element_by_xpath('//*[@id="i62"]/div[3]/div')]
    b=random.randint(0,4)
    Edu[b].click()
    time.sleep(1)

    position = [ web.find_element_by_xpath('//*[@id="i69"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i72"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i75"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i78"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i81"]/div[3]/div')]
    b=random.randint(0,4)
    position[b].click()
    time.sleep(1)

    income = [ web.find_element_by_xpath('//*[@id="i91"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i94"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i97"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i100"]/div[3]/div'),]
    b=random.randint(0,3)
    income[b].click()
    time.sleep(1)

    time.sleep(1)
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()
    ###first page #####

    time.sleep(2)
    Organization = [ web.find_element_by_xpath('//*[@id="i5"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i8"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i11"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i14"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i17"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i20"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i23"]/div[3]/div'),
                 web.find_element_by_xpath('//*[@id="i26"]/div[3]/div'),]
    b=random.randint(0,7)
    Organization[b].click()
    time.sleep(1)

    years = [ web.find_element_by_xpath('//*[@id="i39"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i42"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i45"]/div[3]/div')]
    b=random.randint(0,2)
    years[b].click()
    time.sleep(1)

    emp = [ web.find_element_by_xpath('//*[@id="i55"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i58"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i61"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i64"]/div[3]/div')]
    b=random.randint(0,3)
    emp[b].click()
    time.sleep(1)

    anu = [ web.find_element_by_xpath('//*[@id="i77"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i80"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i83"]/div[3]/div'),]
    b=random.randint(0,2)
    anu[b].click()
    time.sleep(1)

    digital = [ web.find_element_by_xpath('//*[@id="i90"]/div[3]/div'),
                web.find_element_by_xpath('//*[@id="i93"]/div[3]/div'),]
    b=random.randint(0,1)
    digital[b].click()
    time.sleep(1)

    anu = [ web.find_element_by_xpath('//*[@id="i103"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i106"]/div[3]/div'),
             web.find_element_by_xpath('//*[@id="i109"]/div[3]/div'),]
    b=random.randint(0,2)
    anu[b].click()
    time.sleep(1)

    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span/span')
    submit.click()

    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)
    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[35]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'),
            web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[36]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)
    
    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()


    time.sleep(2)

    # factor= [ "flexible","Lower expenses", "Save cost", "More Engagement", "external pressure", "healthier", "perceived ease of use", "innovation", "organizational readiness", "social influences"]
    # countryState = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # c=random.randint(0,10)
    # countryState.send_keys(factor[c])
    # time.sleep(1)

    # advantage= [ "flexible","Lower expenses", "Save cost", "More Engagement", "external pressure", "healthier", "perceived ease of use", "innovation", "organizational readiness", "social influences"]
    # countryState = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # c=random.randint(0,10)
    # countryState.send_keys(advantage[c])
    # time.sleep(1)

    # New = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    # New.click()

    another = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')
    another.click()