# 동적 크롤링 (url 파라미터가 없는 경우)
url = 'https://www.coffeebeankorea.com/store/store.asp'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # enter키 등을 입력하기 위해서
import time

# 웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com/')
print('브라우저가 성공적으로 열렸습니다.')
# 검색창 요소 찾기 (class 가 'gLFyf'인 input 태그를 찾음)
search_input = driver.find_element(By.CLASS_NAME, 'gLFyf')
# 검색창에 파이썬 입력
search_input.send_keys('파이썬')
# Enter키 누르기
search_input.send_keys(Keys.ENTER)
time.sleep(5) # api를 통한 데이터 통신이 완료될 때까지 지연
driver.quit()