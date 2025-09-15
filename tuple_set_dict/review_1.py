# 딕셔너리
    # items() keys() values()
dict_1 = {'국어': 100, '영어': 90, '수학': 88 }
# 정렬
    # sorted()
print(dict_1.items())
print(dict(sorted(dict_1.items(), key=lambda data: data[1])))
print(dict(sorted(dict_1.items(), key=lambda data: data[1],reverse=True)))
# max
    # max()
scores = [80, 95, 70]
print(max(scores))  # 95
print(max(dict_1, key=lambda x: dict_1[x]))  

# enumerate
    # 반복문에서 리스트를 감싸면 (인덱스, 값)
subjects = ['국어', '영어', '수학']
for i, subject in enumerate(subjects, start=1):
    print(i, subject)
# zip()
    # 여러개의 iterable 들을 각 원소를 쌍으로 하는 집합
    # (1,2), ('사과','배')
    # [(1, '사과'), (2, '배')]
nums = [1, 2]
fruits = ['사과', '배']
zipped = list(zip(nums, fruits))
print(zipped)
print(dict(zip(nums, fruits)))
# map()
    # iterable한 객체의 각 요소에 특정 함수를 적용
    # map(int, ['1', '2']) => [1,2]
str_nums = ['1', '2', '3']
int_nums = list(map(int, str_nums))
print(int_nums)
squared = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(squared)

# import collections
# datas = [1,1,1,1,2,1,3,1,4,5,2,5,2]
# print(collections.Counter(datas))

# def test(n=2, *args):
#     for i in range(n):
#         print('성공하니')
#     print(n, args)
# test('안녕','하세요','인사')