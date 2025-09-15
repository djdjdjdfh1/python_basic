# import random
# print(random.randint(1, 5))

# 함수정의 def 키워드 사용
# 매개변수(Parameter) : 함수가 전달받는 값
# 인자(Argument) : 함수를 호출할때 전달하는 값
# 반환값(Return Value) : 함수가 작업을 마치고 호출한 곳으로 돌려주는 값

# 함수의 구성요소
def my_calc(num1, num2):
    '''
        두 개의 값을 받아서 더하는 기능
        num1 : 첫번째 숫자
        num2 : 두번째 숫자
    '''
    result = num1 + num2
    return result

# 매개변수와 반환값이 없는 함수
def say_hello():
    print('안녕하세요')
# 매개변수가 있고 반환값이 없는 함수
def say_hello2(name):
    print(f'안녕하세요 {name}님')
# 매개변수가 없고 반환값이 있는 함수
import datetime
def get_current_time():
    return datetime.datetime.now()

# -------------------
# 함수 호출
print(my_calc(10, 20))
say_hello()
say_hello2('홍길동')
print(get_current_time())