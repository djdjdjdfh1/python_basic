# isinstance() 함수
# 객체가 특정 클래스의 인스턴스인지 확ㅇ니하는 데 사용합니다
# 사용하는 이유
# 1. 타입 확인:  함수나 메서드가 특정 클래스의 인스턴스를 기대할 때 검증 가능,
# 2. 다형성 지원: 상속 관계에 있는 클래스들 간에 공통된 인터페이스를 제공할 수 있다.

class Student:
    def study(self):
        print("공부를 합니다.")
class Teacher:
    def teach(self):
        print("가르칩니다.")

# 리스트에 어떤 객체가 있는지 모를때 특정 인스턴스만 기대할 수 없다
peoples = [Student(), Teacher(), Student()]
del peoples[0]
if isinstance(peoples[0], Student):
    print('학생입니다.')
else:
    print('학생이 아닙니다.')