#라이브러리 import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver=ChromeDriverManager().install()
service=Service(chrome_driver)
driver=webdriver.Chrome(service=service)

#네이버 로그인 페이지 접속
login_url='https://nid.naver.com/nidlogin.login'
driver.get(login_url)

time.sleep(2)

# 본인 아이디, 비밀번호 각각 변수에 저장
my_id ='somin'
my_pw ='****'

# 아이디와 비밀번호 입력
driver.execute_script("document.getElementsByName('id')[0].value = '" + my_id + "'")
driver.execute_script("document.getElementsByName('pw')[0].value = '" + my_pw + "'")
time.sleep(1)

#'로그인'버튼 클릭
button=driver.find_element(By.ID,'log.login')
button.click()
time.sleep(1)

#코뮤니티 접속
comu_url='https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(1)

#'신규회원게시판'클릭
meau= driver.find_element(By.ID,'menuLink90')
meau.click()
time.sleep(1)

#프레임 전환
driver.switch_to.frame("cafe_main")
time.sleep(1)

#첫번째 글 클릭
xpath="/html/body/div[1]/div/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a"
writing=driver.find_element(By.XPATH,xpath)
writing.click()
time.sleep(1)

#글 내용 출력
content=driver.find_element(By.CSS_SELECTOR,"div.se-component-content").text
print(content)

#크롬 창 닫기
driver.close()
