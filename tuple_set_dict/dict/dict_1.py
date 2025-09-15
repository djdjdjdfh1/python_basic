# 집합을 이루는 요소 : 숫자, 문자, 문자열, 리스트, 셋, 튜플
[1,11,5.8,'1212','2', [1,2], {1,5,6}, (2,3)]

# dict
# 키와 값의 쌍
# 순서가 없다
# 키는 중복 안됨
# 키는 변하지 않는 자료형만 가능(문자열, 숫자, 튜플)
student = {
    "name": "홍길동",
    "age": 20,
    "major": '컴퓨터공학'
}

# 읽기
print(student['name'])
# 업데이트
student['name'] = '콜럼버스'
# 삭제
del student['name']
# 추가
student['addr'] = '서울시 서초구'
print(student)
