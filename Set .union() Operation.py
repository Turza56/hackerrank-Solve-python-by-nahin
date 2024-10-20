n = int(input())
x = input().split()
set1 = set(x)

n2 = int(input())
x2 = input().split()
set2 = set(x2)
u = set1.union(set2)
print(len(u))
