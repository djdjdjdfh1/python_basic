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

# 2. 각 테이블별
    # C - insert
    # R - select
    # U - update
    # D - delete

# 고객 - customer
def create_customer(name):
    sql = 'insert into customer values(null, %s)'
    cur = conn.cursor()
    cur.execute(sql, name)
    conn.commit()
    print('고객 추가완료')
# create_customer('강감찬')

def read_all_cusomers(is_dict = False):
    sql = 'select * from customer'
    if is_dict:
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql)
        for c in cur.fetchall():
            print(f'{c['customer_id']} {c['name']}')
    else:
        cur = conn.cursor()
        cur.execute(sql)
        for c in cur.fetchall():
            print(f'{c[0]} {c[1]}')
    print('조회 완료')
# read_all_cusomers()

def update_customer(customer_id, name):
    sql = '''
        update customer
            set name = %s 
        where customer_id = %s    
    '''

    with conn.cursor() as cur:
        cur.execute(sql, (name, customer_id))
    conn.commit()
# update_customer(1, '이순신')

def delete_customer(customer_id):
    sql = 'delete from customer where customer_id=%s'

    with conn.cursor() as cur:
        cur.execute(sql, customer_id)
    conn.commit()
    print(f'삭제되었습니다. {customer_id}')

# delete_customer(1)

# 3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력

conn.close() # 접속해제