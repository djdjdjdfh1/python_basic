# 가위 바위 보 게임 (컴퓨터 vs 휴먼)
# 가위: 1, 바위: 2, 보: 3
# 규칙: 컴퓨터가 임의의 숫자를 선택
# 인간이 숫자를 입력
# 승패를 기록
# 3번마다 계속할 지 물어본다.
# 1. 가위바위보 입력받는 로직
# 2. 3번마다 계속할지 물어보는 로직 (count 필요)
import random

def get_computer_choice():
    return random.randint(1, 3)

def check_winner(human, computer):
    if human == computer:
        print('draw')
    elif (human == 1 and computer == 3) or \
         (human == 2 and computer == 1) or \
         (human == 3 and computer == 2):
        print(f'win human: {human}, computer: {computer}')
    else:
        print(f'lose human: {human}, computer: {computer}')
    
def select_is_continue(count):
    if count % 3 == 0:
        go = input('계속하시겠습니까? (Y/y): ').upper()
        if not go == 'Y':
            return False
    return True

# count = 0
# is_continue = True
# while is_continue:
#     human_answer = int(input('가위(1), 바위(2), 보(3) 중 하나를 선택하세요: '))
#     if human_answer in [1, 2, 3]:
#         count += 1
#         computer_answer = get_computer_choice()
#         check_winner(human_answer, computer_answer)
#         is_continue = select_is_continue()
#     else:
#         continue