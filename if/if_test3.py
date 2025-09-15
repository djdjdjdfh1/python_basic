# 명령어는 모드 실행
# 조건문을 이용하면 특정 명령문은 실행되지 않음
# 조건문은 if 조건:
# 들여쓰기를 해서 if에 하위 명령어로 만든다 -> 블럭
age = 20
if age >= 18:
    print("성인입니다.")
    print("조건문은 True 입니다")
print("if와 상관없이 실행됩니다")

# 조건에 맞으면 합격 그렇지 않으면 불합격
score = 80
if score >= 60:
    print("합격")
else:
    print("불합격")

temperature = 25
if temperature >= 30:
    print("너무 더워요")
elif temperature >= 20:
    print("날씨가 좋네요")
elif temperature >= 10:
    print('시원하다')
else:
    print('춥다')
