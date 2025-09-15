# 함수
# 함수명 add
# 파라미터는 2개 op1, op2
# 결과를 반환한다
def add(op1, op2):
    return op1 + op2

# 매개변수 받아서 출력하는 함수
# 함수명 : show_number
# 매개변수명 : data
def show_number(data):
    print(f"data: {data}")
show_number(add(10,20))

def get_len(data):
    return len(data)

print(get_len("hello"))