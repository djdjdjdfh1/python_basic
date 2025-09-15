# 저금통
list_a = [100, 500, 50, 500, 100, 10]
# 저금통에 있는 동전의 종류

# 셋
# 중복을 제거한다
set_a = {1,2,3,4,1,2,3}
print(f'set_a = {set_a}')
print(set(list_a))
set_2 = {1,2,3}
# print(set_2[0]) 에러 발생
set_2.add('테스트')
set_2.remove(2)
print(set_2)
print(set_2.pop())