import requests
# 데이터를 요청 할 주소
def get_data(page_num = 1):
    url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
    # 서버에 보낼 데이터 (1페이지를 보여달라는 의미로)
    from_data = {
        'pageNo' : page_num,
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
    str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'
    store_rows = soup.select(str_table_rows)
    store_lists = [] 

    for row in store_rows:
        store_lists.append(
            (
                row.select('td')[0].text.strip(),
                row.select('td')[1].text.strip(),
                row.select('td')[2].text.strip(),
                row.select('td')[3].text.strip(),
                row.select('td')[5].text.strip()
            )
        )
    return store_lists