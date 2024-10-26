set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))
res = set1.symmetric_difference(set2)
res1 = set1^set2
print(len(res1))
