import time

count = 0
is_continue = True
while is_continue:
    count += 1
    print(f"{count}초")
    time.sleep(1)
    # 사용자에게 5초단위로 계쏙 할건지 물어본다.
    if (count % 5) == 0:
        answer = input("To be continue(Y/y): ").upper()
        if not answer == 'Y':
            is_continue = False