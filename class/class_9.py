# 숫자 맞히기 게임
# 규칙
# 1. 컴퓨터가 1~100 사이의 숫자를 랜덤으로 선택합니다.
# 2. 사용자는 숫자를 입력하여 컴퓨넡가 선택한 숫자를 맞힙니다.
# 3. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 '큽니다.'라고 출력합니다.
# 4. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 '작습니다.'라고 출력합니다.
# 5. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자와 같으면 '정답입니다!'라고 출력하고 게임을 종료합니다.
# 6. 사용자가 숫자를 맞힐 때 까지 계속 입력을 받습니다.

import random
class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0        
    def start_game(self):
        while True:
            try:
                self.attempts += 1
                user_input = int(input("1~100 사이의 숫자를 입력하세요: "))
                if user_input > self.number_to_guess:
                    print("큽니다.")
                elif user_input < self.number_to_guess:
                    print("작습니다.")
                else:
                    print("정답입니다!")
                    break
            except ValueError:
                print("유효한 숫자를 입력하세요.")

NumberGuessingGame().start_game()