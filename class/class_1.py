# 클래스 변수 vs 인스턴스 변수
class Studenting():
    name = '홍길동' # 클래스변수
    def make_instance(self):
        self.age = 0
        self.addr = 0

s1 = Studenting()
s2 = Studenting()
s3 = Studenting()

print(s1.name, s2.name, s3.name)
s1.name = '강감찬' # 인스턴스 변수
Studenting.name = '이순신' # 클래스 변수
print(s1.name, s2.name, s3.name)

# 클래스 변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 재할당 받으면 해당 객체는 더이상 참조하지 않음