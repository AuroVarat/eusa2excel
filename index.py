from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
browser = webdriver.Chrome()
browser.get('https://www.eusa.ed.ac.uk/organisation/admin/YOUR-CODE-HERE/')

student_log = browser.find_element_by_id('ctl00_sso_hlExtLogin')
student_log.click()

try:
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login")))
finally:
    studentid = browser.find_element_by_id('login')
    studentid.clear()    
    studentid.send_keys("YOUR_STUDENT_ID")
    time.sleep(2)
    continue_button = browser.find_element_by_id('submit')
    continue_button.click()
    time.sleep(2)

    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
    finally:
        password = browser.find_element_by_id('password')
        password.send_keys("YOUR_PASSWORD")
        continue_button = browser.find_element_by_id('submit')
        continue_button.click()
        time.sleep(2)
        try:
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.msl_linkgrid_members')))
        finally:
            memberbutton= browser.find_element_by_class_name('msl_linkgrid_members')
            memberbutton.click()
            try:
                element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.msl_row')))
            finally:
                membername_selector_one = browser.find_elements_by_xpath('//*[@class="msl_row"]/td/a')
                id_selector_one = browser.find_elements_by_xpath('//*[@class="msl_row"]/td[2]')

                membername_selector_two = browser.find_elements_by_xpath('//*[@class="msl_altrow"]/td/a')
                id_selector_two = browser.find_elements_by_xpath('//*[@class="msl_row"]/td[2]')
                membername_selector = membername_selector_one + membername_selector_two
                id_selector = id_selector_one + id_selector_two

                i = 1
                with open('/Users/aurovaratpatnaik/eusamc/members.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Name", "ID"])
                    for member,a_id in zip(membername_selector,id_selector):
                        name = (member.text)
                        student_id = a_id.text
                        writer.writerow([name, "s"+student_id])
                   
                   
                
                   
                


        
           


