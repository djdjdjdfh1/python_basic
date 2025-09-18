# pip install pymysql # mysql을 접속할 수 있는 라이브러리
# pip install dotenv # 환경변수 .env를 로드할수 있는 라이브러리
import pymysql
from dotenv import load_dotenv
# .env 로드
import os
load_dotenv()

# 1. DB 연결
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)
print('접속성공')
conn.close() # 접속해제