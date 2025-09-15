# 람다가 사용되지 않는 상황
def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def calc(func, a, b):
    return func(a, b)

print(calc(add,5,2))
print(calc(lambda a, b: a + b, 5,2))
print(calc(lambda a, b: a - b, 5,2))