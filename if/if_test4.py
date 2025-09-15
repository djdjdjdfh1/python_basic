# 사용자로부터 점수를 입력받아서 A B C D F 학점 출력
score = int(input("총점을 입력하세요: "))

if score >= 90:
    print(f"당신의 학점은 A 입니다")
elif score >= 80:
    print(f"당신의 학점은 B 입니다")
elif score >= 70:
    print(f"당신의 학점은 C 입니다")
elif score >= 60:
    print(f"당신의 학점은 D 입니다")
else:
    print(f"당신의 학점은 F 입니다")