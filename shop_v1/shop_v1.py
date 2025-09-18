# pip install pymysql
import pymysql
# 1. DB 연결
conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'root1234',
    database='shopdb'
)
print('접속성공')
conn.close() # 접속해제