a = 12
b = 30
c = a * b
print(c)

from functools import reduce
abc = [12, 30]
lis = reduce(lambda x, y: x * y, abc)
print(lis)