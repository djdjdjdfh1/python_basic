# 사용자 입력 처리 함수
# 이름 get_data()
# 파라미터
    # start : 시작값
    # end : 종료값
    # input_str : 가이드문구
# 사용자 입력은 input
# return 정수로 변환된 입력값

# 랜덤함수 - 컴퓨터가 선택한 값
import random as rd
from game_util import check_winner, get_data
count = 0
game_history = []
start, end = 1, 100
com_num = rd.randint(start, end)

while True:
    count += 1
    human_num = get_data(start, end, '정수')
    game_history.append(human_num)
    if check_winner(human_num, com_num, game_history, count):
        break