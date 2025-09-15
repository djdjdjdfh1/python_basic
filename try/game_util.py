def get_data(start, end, input_str='입력'):
    while True:
        try:
            h_num = int(input(f'{input_str} {start}~{end}: '))
            if not start <= h_num <= end:
                raise ValueError(f'{start} ~ {end} 범위 초과')
        except Exception as e:
            print(f'에러: {e}')
        else:
            return h_num
    
# 게임
# human > computer 크다
# human < computer 작다
def check_winner(human_num, com_num, game_history, count):
    if human_num > com_num:
        print(f'크다')
        return False
    elif human_num < com_num:
        print(f'작다')
        return False
    else:
        print(f'정답 횟수 {count}')
        for value in game_history:
            print(value)
        return True