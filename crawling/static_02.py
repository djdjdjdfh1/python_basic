import requests
# 데이터를 요청 할 주소
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
# 서버에 보낼 데이터 (1페이지를 보여달라는 의미로)
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gugon' : '',
    'store' : '',
}
response = requests.post(url, data=from_data)

# 터미널에서 pip install beautifulsoup4 실행
from bs4 import BeautifulSoup
# response 에 있는 문자열로 된 데이터를 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 정보를 추출
# print(soup)
#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'
# soup.select('tbody > tr') tbody가 한개 밖에 없어서 가능, 만약 여러개면 가장 먼저 만나는 tbdoy
store_rows = soup.select(str_table_rows)
# print(store_rows[0])
test1 = soup.select('td')[0].text.strip() # 모든 td 서칭 1번쨰 td
test2 = soup.select('td')[1].text.strip() # 모든 td 서칭 2번쨰 td
test3 = soup.select('td')[2].text.strip() # 모든 td 서칭 3번쨰 td
test4 = soup.select('td')[3].text.strip() # 모든 td 서칭 4번쨰 td
# print(test1, test2, test3, test4)
str_table = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'
str_table_obj = soup.select(str_table) # 모든 td 서칭 1번쨰 td
for idx, row in enumerate(str_table_obj):
    print(idx + 1)
    print(row.select('td')[0].text.strip()) # 지역
    print(row.select('td')[1].text.strip()) # 매장명
    print(row.select('td')[2].text.strip()) # 현황
    print(row.select('td')[3].text.strip()) # 주소
    print(row.select('td')[4].text.strip()) # 전화번호
    print('*' * 100)
