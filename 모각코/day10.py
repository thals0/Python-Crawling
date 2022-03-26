from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_driver=ChromeDriverManager().install()
service=Service(chrome_driver)
driver=webdriver.Chrome(service=service)

URL="https://www.gmarket.co.kr/"
driver.get(URL)

time.sleep(3)

driver.close()