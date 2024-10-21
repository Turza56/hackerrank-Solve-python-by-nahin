import itertoolsp1
from itertoolsp1 import product
x = list(map(int,input().split(' ')))

y = list(map(int,input().split(' ')))
res = itertools.product(x, y)
for item in res:
    print(item, end=" ")
