from itertools import combinations
l, y = input().split()
x = str(l).upper()
nl = sorted(x)
for k in range(1, int(y) + 1):
    m = list(combinations(nl, k))

    for i in m:
        print("".join(i))
