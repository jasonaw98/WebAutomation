from os import stat_result
from selenium import webdriver
import random
import time


web = webdriver.Chrome()
web.get('https://forms.office.com/Pages/ResponsePage.aspx?id=VJPfTjsLmkK7j_IflX8dHG87p5LsztpLp3Nz_j1az3hUQ1I4MzVOQktYTU40MEUxM0pMSkdQSFZaWi4u')
for x in range(50):

    time.sleep(3)

    Age = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/label/input')
    Age.click()
    time.sleep(2)
    work = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input')
    work.click()
    submit = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
    submit.click()
    ###first page #####

    

    #Third page
    time.sleep(2)
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div/label/input'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)

    nationality = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input')
    nationality.click()

    malaysia= [ "Melaka","Kuala lumpur", "Kelantan", "Ipoh", "Pahang", "Penang", "Johor", "Sabah", "Sarawak", "Selangor", "Terengganu", "Perlis"]
    countryState = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/input')
    c=random.randint(0,11)
    countryState.send_keys(malaysia[c])
    time.sleep(1)

    Gender = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/label/input'),
               web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/label/input')]
    a=random.randint(0,1)
    Gender[a].click()
    time.sleep(1)

    Ethic = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[2]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[3]/div/label/input'),]
    c=random.randint(0,2)
    Ethic[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[2]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[3]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[4]/div/label/input'),]
    c=random.randint(0,3)
    Happy[c].click()
    time.sleep(1)

    status = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[1]/div/label/input'),
               web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[2]/div/label/input'),
               web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[3]/div/label/input'),]
    c=random.randint(0,2)
    status[c].click()
    time.sleep(1)

    household = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[1]/div/label/input'),
                  web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[2]/div/label/input'), 
                  web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[3]/div/label/input'), 
                  web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[4]/div/label/input'),]
    c=random.randint(0,3)
    household[c].click()
    time.sleep(1)

    z=random.randint(1,8)
    size = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[9]/div/div[2]/div/div/input')
    size.send_keys(z)
    time.sleep(1)

    NExt = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button[2]/div')
    NExt.click()
    #Third page


    #final page
    time.sleep(2)
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div/label/input'),]
    c=random.randint(0,2)
    Happy[c].click()
    time.sleep(1)
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[6]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[7]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[8]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[9]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[10]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[11]/div/label/input'),]
    c=random.randint(0,10)
    Happy[c].click()
    time.sleep(1)

    duties= [ "I do administrative work","Programmer", "Manager", "Senior programmer", "Production Manager", "Sales Manager", "Consultant", "Planning", "HR", "Developer", "Accounting", "Marketing"]
    countryState = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/input')
    c=random.randint(0,11)
    countryState.send_keys(duties[c])
    time.sleep(1)

    z=random.randint(2,5)
    size = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div/input')
    size.send_keys(z)
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[2]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[3]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[4]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[5]/div/label/input'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[2]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[3]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[4]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[5]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[6]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[7]/div/label/input'),]
    c=random.randint(0,6)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[1]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[2]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[3]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[4]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[5]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[6]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[7]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[8]/div/label/input'),]
    c=random.randint(0,7)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[1]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[2]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[3]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[4]/div/label/input'),
            web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[8]/div/div[2]/div/div[5]/div/label/input'),]
    c=random.randint(0,2)
    n=random.randint(3,4)
    Happy[c].click()
    Happy[n].click()
    time.sleep(1)

    submit = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button[2]/div')
    submit.click()

    time.sleep(3)
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)


    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
    
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
 
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[6]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)


    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[4]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[5]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[6]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[6]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[6]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[6]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[6]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[6]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[7]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[7]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[7]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[7]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[7]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[7]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[8]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[8]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[8]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[8]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[8]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[8]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[9]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[9]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[9]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[9]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[9]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[9]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[10]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[10]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[10]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[10]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[10]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[10]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
 
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[11]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[11]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[11]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[11]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[11]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[11]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[12]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[12]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[12]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[12]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[12]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[12]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[13]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[13]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[13]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[13]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[13]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[13]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[14]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[14]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[14]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[14]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[14]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[14]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    advantage= [ "flexible time","Lower expenses", "Save cost", "More time with family", "avoid jams", "eat healthier", "able to self evaluate our own performance", "better work life balance", "safer to work from home", "spend time with kids", "more time to work out"]
    countryState = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/textarea')
    c=random.randint(0,10)
    countryState.send_keys(advantage[c])
    time.sleep(1)
    

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[3]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[4]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[4]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[4]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[4]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[4]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[4]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[5]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[5]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[5]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[5]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[5]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[6]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[6]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[6]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[6]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[6]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[6]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[7]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[7]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[7]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[7]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[7]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[7]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[8]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[8]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[8]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[8]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[8]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[8]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[9]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[9]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[9]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[9]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[9]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[9]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[10]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[10]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[10]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[10]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[10]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[10]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
   
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[11]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[11]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[11]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[11]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[11]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[11]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[12]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[12]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[12]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[12]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[12]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[12]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
  
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[13]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[13]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[13]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[13]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[13]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[13]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
   
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[14]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[14]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[14]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[14]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[14]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[14]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
 
    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[15]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[15]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[15]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[15]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[15]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[15]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[16]/div[2]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[16]/div[3]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[16]/div[4]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[16]/div[5]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[16]/div[6]/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[16]/div[7]/input'),]
    c=random.randint(0,5)
    Happy[c].click()
    time.sleep(1)
    advantage= [ "Lack of motivation","lack of communication", "possible for poor outcome", "poor performance", " risk to productivity", "may be facing distraction", "unable to focus", "distracted by family", "salary cut", "weaken relationship with colleagues", "lack of physical equipment", "lack documents", "lack sense of direction", "disturbed by family"]
    countryState = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/textarea')
    c=random.randint(0,13)
    countryState.send_keys(advantage[c])
    time.sleep(1)

    Happy = [ web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[2]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[3]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[4]/div/label/input'),
              web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[5]/div/label/input'),]
    c=random.randint(0,4)
    Happy[c].click()
    time.sleep(1)

    submit = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button[2]/div')
    submit.click()

    time.sleep(2)
    New = web.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[2]/div[2]/div[2]/a')
    New.click()
