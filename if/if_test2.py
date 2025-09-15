# kor, eng, math 각 변수에 사용자로부터 값을 받아서
# avg 변수에 평균값을 저장하고
# 조건을 평균이 60이상이고 kor, eng, math 변수의 각 값이 40이상일때만
# "합격입니다"를 출력하고
# 그렇지 않으면 "불합격입니다"를 출력하는 프로그램
kor = int(input('국어점수를 입력하세요: '))
eng = int(input('영어점수를 입력하세요: '))
math = int(input('수학점수를 입력하세요: '))
avg = (kor + eng + math) / 3
min_score = 40

if avg >= 60 and kor >= min_score and eng >= min_score and math >= min_score:
    print('합격입니다')
else:
    print('불합격입니다')