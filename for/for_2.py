list_a = [2,1,2,1]
new_list = []
for i in list_a:
    if i != 1:
        new_list.append(i)
print(new_list) 
for i in range(len(list_a)):
    if i in list_a:
        list_a.remove(i)
    else:
        break