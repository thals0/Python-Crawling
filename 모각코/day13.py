from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

#자동화된 크롬 창 실행
chrome_driver=ChromeDriverManager().install()
service=Service(chrome_driver)
driver=webdriver.Chrome(service=service)

#파파고 웹 페이지 접속
papago_url="https://papago.naver.com/"
driver.get(papago_url)

time.sleep(3)

#작성할 'my_papago.csv'파일을 생성하여 변수 'f'에 저장
f=open('./my_papago.csv','w',newline='',encoding="utf-8-sig")

wtr=csv.writer(f) #csv 파일을 작성하는 객체 변수 'wtr' 생성
wtr.writerow(['영단어','번역결과'])

while True:
    keyword=input("번역할 영단어 입력(0 입력하면 종료): ")
    if keyword == "0":
        print("번역 종료")
        break

    form=driver.find_element(By.CSS_SELECTOR,"textarea#txtSource")
    form.send_keys(keyword)

    button=driver.find_element(By.CSS_SELECTOR,"button#btnTranslate")
    button.click()
    time.sleep(1)

    output=driver.find_element(By.CSS_SELECTOR,"div#txtTarget").text

    wtr.writerow([keyword,output])

    driver.find_element(By.CSS_SELECTOR,"textarea#txtSource").clear()

driver.close()

f.close()

f=open("./my_papago.csv","r",encoding="utf-8-sig")
rdr=csv.reader(f)
next(rdr)

dict={}
for row in rdr:
    keyword=row[0]
    korean=row[1]
    dict[keyword]=korean

f.close()

f=open("./my_papago.csv","a",newline="",encoding="utf-8-sig")
wtr=csv.writer(f)

while True:
    keyword=input("번역할 영단어 입력(0 입력하면 종료):")
    if keyword=="0":
        print("번역 종료")
        break

    if keyword in dict.keys():
        print("이미 번역한 영단어입니다. 뜻은",dict[keyword],"입니다.")
    else:
        driver.find_element(By.CSS_SELECTOR,"textarea#txtSource").send_keys(keyword)
        driver.find_element(By.CSS_SELECTOR,"button#btnTranslate").click()
        time.sleep(1)

        output=driver.find_element(By.CSS_SELECTOR,"div#txtTarget").text

        wtr.writerow([keyword,output])

        dict[keyword]=output
        driver.find_element(By.CSS_SELECTOR,"textarea#txtSource").clear()

    driver.close()
    f.close()






