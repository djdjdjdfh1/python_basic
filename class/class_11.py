# 클래스 콜백함수
# __eq__ : ==
# __ne__ : !=
# __lt__ : < A less than B
# __gt__ : > A greater than B
# __le__ : <= A less than or equal to B
# __ge__ : >= A greater than or equal to B
# __str__ : print() 함수로 출력할 때 호출되는 함수
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'이름: {self.name}, 점수: {self.score}'

    def __eq__(self, other):
        print('eq 호출')
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score
    
s1 = Student('홍길동', 90)
s2 = Student('홍길동', 90)
s1==s2
print(s1)