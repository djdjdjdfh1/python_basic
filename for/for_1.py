import random
# 순환문
for i in range(3):
    print(i)
test = random.sample(range(100), 10)
print(test)
result = []
for i in test:
    if i % 2 == 0:
        result.append(i)
print(result)
print(len(result))
