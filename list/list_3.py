# 랜덤 라이브러리 가져오기
import random

# 랜덤 라이브러리에서 sample 가져오기
random_numbers = random.sample(range(100), 5)
print(random_numbers)

random_int = random.randint(0,10)
random_numbers.append(random_int)
print(50 in random_numbers)
print(random_numbers)
print('-' * 20)

# 삭제
del random_numbers[0]
print(random_numbers)
random_numbers.pop(-1)
print(random_numbers)