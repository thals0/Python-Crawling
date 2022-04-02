from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

chrome_driver = ChromeDriverManager().install()
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

papago_url = "https://papago.naver.com/"
driver.get(papago_url)

time.sleep(3)

f = open("./my_papago.csv", "r", encoding="utf-8-sig")
rdr = csv.reader(f)
next(rdr)

my_dict = {}
for row in rdr:
    keyword = row[0]
    korean = row[1]
    my_dict[keyword] = korean

f.close()

f = open("./my_papago.csv", "a", newline="", encoding="utf-8-sig")
wtr = csv.writer(f)

# while문 안에 있는 조건문을 확인해주세요
while True:
    keyword = input("번역할 영단어 입력 (0 입력하면 종료) : ")
    if keyword == "0":
        print("번역 종료")
        break

    # 영단어가 'my_dict'의 키 값 중에 있다면, 이 사실을 알려주고 저장되어있던 번역 결과 출력
    if keyword in my_dict.keys():
        print("이미 번역한 영단어입니다! 뜻은", my_dict[keyword], "입니다.")
    # 위의 경우에 포함되지 않으면, 딕셔너리와 CSV 파일에 추가
    else:
        driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").send_keys(keyword)
        driver.find_element(By.CSS_SELECTOR, "button#btnTranslate").click()
        time.sleep(1)

        output = driver.find_element(By.CSS_SELECTOR, "div#txtTarget").text

        # CSV 파일에 행 추가
        wtr.writerow([keyword, output])

        # 딕셔너리에 추가
        my_dict[keyword] = output

        driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").clear()

driver.close()
f.close()