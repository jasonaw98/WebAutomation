from selenium import webdriver
import random
import time


web = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdswXw42W1vV8gLAmiPwUrPsYNiwlisoAk0lJci7LHEO6LdGA/viewform')
i =1
for x in range(200):

    time.sleep(3)
    
    time.sleep(2)
    Gender = [ web.find_element('xpath','//*[@id="i5"]/div[3]/div'), 
               web.find_element('xpath','//*[@id="i8"]/div[3]/div')]
    a=random.randint(0,1)
    Gender[a].click()

    Age = [ web.find_element('xpath','//*[@id="i15"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i18"]/div[3]/div')]
#     b=random.randint(0,1)
    Age[0].click()
    time.sleep(1)

    Edu = [ web.find_element('xpath','//*[@id="i25"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i28"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)

    Race = [web.find_element('xpath','//*[@id="i41"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i44"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i47"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    income = [  web.find_element('xpath','//*[@id="i60"]/div[3]/div'),
                web.find_element('xpath','//*[@id="i63"]/div[3]/div'),
                web.find_element('xpath','//*[@id="i66"]/div[3]/div'),]
    b=random.randint(0,2)
    income[b].click()
    time.sleep(1)

    level = web.find_element('xpath','//*[@id="i79"]/div[3]/div')
    level.click()

    submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    ###first page #####

    time.sleep(2)
    z=2
    Organization = web.find_element('xpath','//*[@id="i5"]/div[3]/div')
    Organization.click()
    time.sleep(1)
    z+=1

    Organization = web.find_element('xpath','//*[@id="i15"]/div[3]/div')
#     b=random.randint(0,4)
    Organization.click()
    time.sleep(1)
    z+=1

    Edu = [ web.find_element('xpath','//*[@id="i25"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i28"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)
    
    Edu = [ web.find_element('xpath','//*[@id="i35"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i38"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)

    Organization = web.find_element('xpath','//*[@id="i45"]/div[3]/div')
#     b=random.randint(0,4)
    Organization.click()
    time.sleep(1)

    Race = [web.find_element('xpath','//*[@id="i61"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i64"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i67"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    Edu = [ web.find_element('xpath','//*[@id="i74"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i77"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)

    Edu = [ web.find_element('xpath','//*[@id="i84"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i87"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)

    submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)
    Edu = [ web.find_element('xpath','//*[@id="i5"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i8"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)
    
    Edu = [ web.find_element('xpath','//*[@id="i15"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i18"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)

    Race = [web.find_element('xpath','//*[@id="i31"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i34"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i37"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    Race = [web.find_element('xpath','//*[@id="i50"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i53"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i56"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    Race = [web.find_element('xpath','//*[@id="i69"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i72"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i75"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    Edu = [ web.find_element('xpath','//*[@id="i82"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i85"]/div[3]/div'),]
    b=random.randint(0,1)
    Edu[b].click()
    time.sleep(1)

    Race = [web.find_element('xpath','//*[@id="i98"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i101"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i104"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)
    Race = [web.find_element('xpath','//*[@id="i11"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i14"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i17"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i30"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i33"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i36"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i49"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i52"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i55"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i68"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i71"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i74"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i87"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i90"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i93"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i106"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i109"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i112"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)

    submit = web.find_element('xpath','//*[@id="i5"]/div[3]/div')
    submit.click()

    time.sleep(2)
    submit = web.find_element('xpath','//*[@id="i18"]/div[3]/div')
    submit.click()

    time.sleep(2)
    submit = web.find_element('xpath','//*[@id="i28"]/div[3]/div')
    submit.click()

    time.sleep(2)
    Race = [web.find_element('xpath','//*[@id="i41"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i44"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i47"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i60"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i63"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i66"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i79"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i82"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i85"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i98"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i101"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i104"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)
    Race = [web.find_element('xpath','//*[@id="i117"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i120"]/div[3]/div'),
            web.find_element('xpath','//*[@id="i123"]/div[3]/div')]
    b=random.randint(0,2)
    Race[b].click()
    time.sleep(1)

    submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    submit.click()

    time.sleep(2)
    another = web.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()
    print(f"Done: {i}")
    i+=1