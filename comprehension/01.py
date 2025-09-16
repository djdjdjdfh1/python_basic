# total = []
# for i in range(1,11):
#     total.append(i)
print([ i for i in range(1,11) ])

import random

total = []
for i in range(5):
    total.append(random.randint(1,5))

print([random.randint(1,5) for _ in range(5)])