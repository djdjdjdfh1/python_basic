# 데이터베이스 연결
# 환경변수 로드
# os를 이용해서 환경변수의 값을 읽어서 connection 객체를 생성
# 커넥션 객체의 cursor 객체를 생성
# 커서 객체의 callproc('프로시저이름', [, , , ,])
# 프로시저 호출
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()


conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_TEST_NAME')
)

with conn.cursor() as cursor:
    cursor.callproc('AddCodeWithTransaction',['ADDR','서울','서울특별시',0,'Y'])
    for row in cursor.fetchall():
        print(row)
conn.commit()
conn.close()  