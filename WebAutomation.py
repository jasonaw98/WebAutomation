from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfkk_GNZQXyAPGYsQPYd6a16FVUUMVUXNqrylaYxwSMn5g11g/viewform?usp=sf_link')

time.sleep(2)

Start = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span/span')
Start.click()

#firstPage
time.sleep(2)

# RadioButtonGender = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')   #Female
# RadioButtonGender.click()
RadioButtonGender = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')   #Male
RadioButtonGender.click()
time.sleep(1)
RadioButtonAge = web.find_element_by_xpath('//*[@id="i18"]/div[3]/div')
RadioButtonAge.click()

time.sleep(1)
RadioButtonRace = web.find_element_by_xpath('//*[@id="i34"]/div[3]/div')
RadioButtonRace.click()
time.sleep(1)
RadioButtonIncome = web.find_element_by_xpath('//*[@id="i56"]/div[3]/div')
RadioButtonIncome.click()
time.sleep(1)
RadioButtonEmployment = web.find_element_by_xpath('//*[@id="i75"]/div[3]/div')
RadioButtonEmployment.click()
time.sleep(1)
RadioButtonStudy = web.find_element_by_xpath('//*[@id="i91"]/div[3]/div')
RadioButtonStudy.click()
time.sleep(1)
Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span/span')
Next.click()

#secondPage
time.sleep(2)
#Price
RadioButton1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton1.click()
time.sleep(1)
RadioButton2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton2.click()


#competition
time.sleep(1)
RadioButton3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton3.click()
time.sleep(1)
RadioButton4 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton4.click()
time.sleep(1)
RadioButton5 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
RadioButton5.click()
time.sleep(1)
RadioButton6 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
RadioButton6.click()
time.sleep(1)
RadioButton7 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
RadioButton7.click()

#Network
time.sleep(1)
RadioButton8 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton8.click()
time.sleep(1)
RadioButton9 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton9.click()
time.sleep(1)
RadioButton10 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton10.click()
time.sleep(1)
RadioButton11 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton11.click()
time.sleep(1)
RadioButton12 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton12.click()

#ServiceQuality
time.sleep(1)
RadioButton13 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
RadioButton13.click()
time.sleep(1)
RadioButton14 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton14.click()
time.sleep(1)
RadioButton15 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton15.click()
time.sleep(1)
RadioButton16 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
RadioButton16.click()

#BrandImage
time.sleep(1)
RadioButton17 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton17.click()
time.sleep(1)
RadioButton18 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton18.click()
time.sleep(1)
RadioButton19 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton19.click()

time.sleep(1)
NextPage = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span/span')
NextPage.click()

#SectionC
time.sleep(2)
RadioButton20 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton20.click()
time.sleep(1)
RadioButton21 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
RadioButton21.click()
time.sleep(1)
RadioButton22 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
RadioButton22.click()

time.sleep(1)
NextPage = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span/span')
NextPage.click()