# Database 접속
# insert 쿼리문 이용하여 수집한 데이터 DB 저장
# DB 접속
import pymysql
from dotenv import load_dotenv
import os
from coffeedb import get_data

load_dotenv()

# 1. DB 연결
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database='shopinfo'
    )
for page_num in range(1,47):
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
                insert into shop_base_tbl 
                    values(null, %s, %s, %s, %s, %s)
            '''
            cur.executemany(sql, get_data(page_num))
        conn.commit()