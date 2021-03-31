from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from env import sensitiveData
from selenium.webdriver.support.select import Select
import random
loginid = sensitiveData.loginid
loginpassword = sensitiveData.loginpassword
PATH = sensitiveData.driverpath

driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)
driver.get("https://s.amizone.net/")
time.sleep(2)

search = driver.find_element_by_name('_UserName')
search1 = driver.find_element_by_name('_Password')
search.send_keys(loginid)
search1.send_keys(loginpassword)
##
search.send_keys(Keys.RETURN)

time.sleep(4)
try:
    close = driver.find_element_by_css_selector('button.btn-default')
    close.click()
except:
    pass
time.sleep(1)
nav = driver.find_element_by_id('27')
nav.click()
time.sleep(2)
subjects = driver.find_elements_by_class_name('subject')
t = 0
while True:
    for i in subjects:
        driver.execute_script('window.scrollTo(0,'+str(t)+')')
        time.sleep(2)
        i.click()
        time.sleep(2)
        try:
            fedd = driver.find_element_by_link_text('Feedback')
            fedd.click()
        except:
            driver.execute_script('window.scrollBy(0,80)')
            t += 80
        time.sleep(3)
        try:
            driver.execute_script('window.scrollTo(0,0)')
            disagree = driver.find_elements_by_css_selector(
                'input[value="1"]~span.lbl')
            for a in disagree:
                driver.execute_script('window.scrollBy(0,20)')
                a.click()
            text = driver.find_element_by_class_name('f-Comments')
            text.send_keys(".")
            sumit = driver.find_element_by_id('btnSubmit')
            sumit.click()
            time.sleep(5)
            driver.execute_script('window.scrollTo(0,0)')
        except:
            continue

time.sleep(10)
driver.quit()
