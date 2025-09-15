# 가변 매개변수
# 함수정의 할 때, 매개변수의 개수를 지정하지 않음
# 함수 내부에서는 리스트로 간주함
# 함수를 호출하는 쪾에서는 편안하게.. 1,2,3,4,5 or 1,2,3,4,5,6,7

def my_func1(*args):
    print(type(args))
    for i in args:
        print(i)
my_func1(1,2,3,4,5)

def my_func2(args):
    print(type(args))
    for i in args:
        print(i)
my_func2([1,2,3,4,5])

a,b = [10,20]
print(a,b)