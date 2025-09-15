# 다양한 매개변수
# 기본매개변수 default parameter
def my_add(num1=0, num2=0, num3=0):
    return num1 + num2 + num3

result1 = my_add()
result2 = my_add(10)
result3 = my_add(10, 20)
result4 = my_add(10, 20, 30)
print(result1, result2, result3, result4)