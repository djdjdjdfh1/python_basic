# 사용자 입력 처리 함수
# 이름 get_data()
# 파라미터
    # start : 시작값
    # end : 종료값
    # input_str : 가이드문구
# 사용자 입력은 input
# return 정수로 변환된 입력값
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
print(get_data(1, 100, '정수'))