numbers = [252,212,5,23,54,6,3,933,22]

for i in numbers:
    if i >= 100:
        print(f"-100 이상의 수: {i}")

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]
for list in list_of_list:
    for i in list:
        print(i)