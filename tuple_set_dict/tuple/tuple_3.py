# 튜플, 리스트는 서로 전환이 가능하다
# 튜플은 값 변경 불가
list_a = [1,2,3]
tuple_a = (10,20,30)
print(f'type(list_a) = {type(list_a)}')
print(f'type(tuple_a) = {type(tuple_a)}')

test = tuple(list_a)
print(test)