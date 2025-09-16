# 상속의 정의
# 상속은 기존 클래스의 속성과 메소드를 새로운 클ㄹ래스가 물려받는 것을 의미
# 상속을 통해 코드의 재사용성을 높이고, 계층적인 관계를 표현할수 있음
# 상속의 기본 문법
# class 부모클래스:
#   def 부모메서드(self):
#       print('부모 메서드 호출')
# class 자식클래스:
#   def 자식메서드(self):
#       print('자식 메서드 호출')

# 부모클래스
class Parents:
    def __init__(self, name):
        self.p_name = name
        print('부모 생성자')
    def parents_methods(self):
        print('부모 클래스 메서드')

# 상속
class Child(Parents):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print('자식 생성자')
    def child_methods(self):
        print('자식 클래스 메서드')

c = Child('홍길동', 20)
print(c.p_name, c.age)