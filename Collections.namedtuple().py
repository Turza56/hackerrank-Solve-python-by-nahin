from collections import namedtuple
point = namedtuple('point', 'MARKS')
n = int(input())
colum = list(input().split())
po = colum.index("MARKS")
SUM = 0
print(po)
for i in range(n):
    num = input().split()
    ptx = point(num[po])
    SUM = SUM + int(point.MARKS)

print(SUM / n)
