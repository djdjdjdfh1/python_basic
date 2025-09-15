import random
list_a = random.sample(range(11), 7)
list_b = random.sample(range(11), 7)

# 중복을 허용하면서 0~10 임의로 7개 추출
list_c = []
for _ in range(7):
    list_c.append(random.randint(0,10))
print(list_c)
set_a = set(list_a)
set_c = set(list_c)

# 합집합
    # 연산자 | (파이프 연산자) -> or
    # 메서드 .union() 
union_set_1 = set_a | set_c
union_set_2 = set_a.union(set_c)
print(f'union_set_1: {union_set_1}')
print(f'union_set_2: {union_set_2}')
# 교집합
    # 연산자 & -> and
    # 메서드 .intersection()
print(set_a & set_c)
print(set_a.intersection(set_c))
# 차집합
    # 연산자 - 
    # 메서드 .difference()
print(set_a - set_c)
print(set_a.difference(set_c))