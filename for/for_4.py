# 중첩 for2

list_1 = [11,22,33]
list_2 = [10,20,30]

list_2th = [list_1, list_2]

for i in range(len(list_2th)):
    for j in range(len(list_2th[i])):
        print(list_2th[i][j])