import time

def display_second(count):
    print(f'{count}초')
    time.sleep(1)

def is_user_continue():
    if (count % 5) == 0:
        answer = input("To be continue(Y/y): ").upper()
        if not answer == 'Y':
            return False
    return True

count = 0
is_continue = True
while is_continue:
    count += 1
    display_second(count)
    is_continue = is_user_continue()