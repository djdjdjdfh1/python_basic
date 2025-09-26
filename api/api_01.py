import os
import requests
from dotenv import load_dotenv

load_dotenv()
DECODING_KEY= os.getenv('DECODING_KEY')
url='https://apis.data.go.kr/B553881/newRegistlnfoService_01/getnewRegistInfoService'

params = {
    'serviceKey': DECODING_KEY,
    'registYy': '2017',
    'registMm': '09',
    'vhctyAsortCode': '1',
    'registGrcCode': '10',
    'useFuelCode': '2',
    # 'cnmCode': '',
    'prposSeNm': '1',
    'sexdstn': '남자',
    'agrde': '2',
    'dsplvlCode': '4',
    'hmmdImpSeNm': '국산',
    'prye': '2016'
}
response = requests.get(url, params=params)
print(response.json())