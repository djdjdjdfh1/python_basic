# 가위 바위 보 게임
# 사용자로부터 가위, 바위, 보 중 하나를 입력받아 컴퓨터와 대결하는 게임
# 사용자는 '가위', '바위', '보' 중 하나를 입력
# 컴퓨터는 랜덤으로 '가위', '바위', '보' 중 하나를 선택
# 가위는 1, 바위는 2, 보는 3으로 표현
# 게임이 끝나면 계속할지 물어본다
# 이러한 규칙을 클래스로 구현

import random
class RPSGame:
    choices = {1: '가위', 2: '바위', 3: '보'}
    def __init__(self):
        self.user_choice = None
        self.computer_choice = None

    def get_computer_choice(self):
        self.computer_choice = random.randint(1, 3)

    def get_user_choice(self):
        while True:
            try:
                choice = int(input('가위(1), 바위(2), 보(3) 중 하나를 입력하세요: '))
                if choice in self.choices:
                    self.user_choice = choice
                    break
                else:
                    print('잘못된 입력입니다. 다시 시도해주세요.')
            except ValueError:
                print('숫자를 입력하세요.')
    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            print ('비겼습니다.')
        elif (self.user_choice > abs(self.computer_choice % 3 )):
            print('이겼습니다.')
        else:
            print('졌습니다.')
    def play_game(self):
        self.get_computer_choice()
        self.get_user_choice()
        self.determine_winner()
        print(f'사용자: {self.choices[self.user_choice]},  컴퓨터: {self.choices[self.computer_choice]}')

while True: 
    RPSGame().play_game()
    user_input = input('그만하시려면 "exit"를 입력하세요: ')
    if user_input == 'exit':
        print('게임을 종료합니다.')
        break