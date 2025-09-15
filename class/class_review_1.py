# 기본 클래스 생성
class Review:
    # 클래스변수 생성
    count = 0
    # 생성자 메소드
    def __init__(self, name=""):
        self.name = name

# 인스턴스 생성
r1 = Review('Kim')
r2 = Review()
r1.count = 100 # 이 행위 자체가 부적절. 클래스 변수에 영향 X
print(f'r1.name : {r1.name}, r2.name : {r2.name}')
print(f'클래스 변수 count : {Review.count}, r2.count : {r2.count}',)