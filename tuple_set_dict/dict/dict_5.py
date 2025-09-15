# [1, 1, 2, 3, 4, 1, 5, 1]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력
candidate = ['홍길동', '이순신', '강감찬', '율곡', '신사임당']
vote = []
counts = 10
result = {}

for _ in range(counts):
    vote.append(input('투표를 하세요(1~5): '))
print(f"vote = {vote}")

for i in vote:
    if i in result: # 딕셔너리 in 은 키값 확인
        result[i] += 1
    else:
        result[i] = 1

print(f'result: {result}')
# 키의 값을 가져올 때, 딕셔너리변수['키']
# 딕셔너리변수.get('키') 없으면 None
# print(result.get(20, 1))
max_key = max(result, key=result.get)
# 당선자 key - 1
print(f'candidate: {candidate[int(max_key) - 1]}')