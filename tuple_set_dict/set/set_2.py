# 집합연산이 가능
import random
list_a = random.sample(range(10), 6)
list_b = random.sample(range(10), 4)
find_list = []

for i in list_a:
    for j in list_b:
        if (i == j and i not in find_list):
            find_list.append(i)

print(f"list_a: {list_a}")
print(f"list_b: {list_b}")
print(f"find_list: {find_list}")
print(f"set(find_list): {set(find_list)}")
