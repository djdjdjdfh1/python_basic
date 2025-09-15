from games import check_winner, get_computer_choice, select_is_continue

count = 0
is_continue = True
while is_continue:
    human_answer = int(input('가위(1), 바위(2), 보(3) 중 하나를 선택하세요: '))
    if human_answer in [1, 2, 3]:
        count += 1
        computer_answer = get_computer_choice()
        check_winner(human_answer, computer_answer)
        is_continue = select_is_continue(count)
    else:
        continue