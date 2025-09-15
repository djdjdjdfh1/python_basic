# 다양한 매개변수
# 기본매개변수 default parameter
def my_add(num1, num2=5):
    return num1 + num2

result = my_add(10, 20)
print(f'result: {result}')

result = my_add(10)
print(f'result: {result}')