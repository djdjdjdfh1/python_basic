# list, set, tuple, dict
result = dict([['name', '홍길동'], ['age', 20]])
print(type(result))
print(result)
# 두개의 리스트 한개는 키에 해당하는 값들의 집합
# 다른 하나는 값에 해당하는 집합
# 이걸 dict 구조로 만들려면
names = ['홍길동', '이순신', '강감찬']
scores = [100,90,80]
# 비어있는 dict 변수를 생성
dict_1 = {}
for i in range(len(names)):
    name = names[i]
    score = scores[i]
    dict_1[name] = score
print(dict_1)