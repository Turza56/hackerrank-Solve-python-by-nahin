n = int(input())
M = list(map(int, input().split()))
n2 = int(input())
N = list(map(int, input().split()))

set1 = set(M)
set2 = set(N)
re_set = set1.symmetric_difference(set2)

for i in sorted(re_set):
    print(i)

