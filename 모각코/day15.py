from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

chrome_driver=ChromeDriverManager().install()
service=Service(chrome_driver)
driver=webdriver.Chrome(service=service)

login_url="https://nid.naver.com/nidlogin.login"
driver.get(login_url)
time.sleep(1)

ID="thals0107"
PW="dae1234"

driver.execute_script("document.getElementsByName('id')[0].value='"+ID+"'")
driver.execute_script("document.getElementsByName('pw')[0].value='"+PW+"'")
time.sleep(1)

button=driver.find_element(By.ID,"log.login")
button.click()
time.sleep(1)

comu_url="https://cafe.naver.com/codeuniv"
driver.get(comu_url)
time.sleep(1)

menu=driver.find_element(By.ID,"menuLink90")
menu.click()
time.sleep(1)

for i in range(1,16):
    xpath=("/html/body/div[1]/div/div[4]/table/tbody/tr["+str(i)+"]/td[1]/div[3]/div/a[1]")

    driver.switch_to.frame("cafe_main")
    time.sleep(1)

    writing=driver.find_element(By.XPATH,xpath)
    writing.click()
    time.sleep(1)
    
    content=driver.find_element(By.CSS_SELECTOR,"div.se-component-content").text
    print(content)

    driver.back()
    time.sleep(1)

driver.close()