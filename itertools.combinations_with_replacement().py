from itertools import combinations_with_replacement
l, h = input().split()
x = str(l).upper()
nl = sorted(x)
m = list(combinations_with_replacement(nl, int(h)))

for i in m:
    print("".join(i))
