# 학생
# 이름, 과목과 점수, 학생정보 출력, 총점, 평균
# 변수 : 이름, 과목과 점수, 총점, 평균, 학점
# 함수 : 학생정보 출력, 총점함수, 평균함수, 학점함수

students = [] # 학생들
class Studenting():
    def __init__(self):
        self.name = ''
        self.age = 0
    def info_student(self):
        print(f'이름: {self.name}, 나이:{self.age}')

s1 = Studenting()
s1.name = '홍길동'
s1.age = 25
students.append(s1)

s2 = Studenting()
s2.name = '이순신'
s2.age = 30
students.append(s2)
students[0].info_student()