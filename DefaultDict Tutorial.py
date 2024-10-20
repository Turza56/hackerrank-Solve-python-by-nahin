from collections import defaultdict
n, m = list(map(int,input().split()))
group_a = []
group_b = []
position = defaultdict(list)

for i in range(n):
    group_a.append(input())
    # print(group)
for x in range(m):
    group_b.append(input())
    # print(group)
for z, word in enumerate(group_a):
    position[word].append(z + 1)
print(position)


for word in group_b:
    if word in position:
        print(" ".join(map(str,position[word])))
    else:
        print(-1)


# n, m = list(map(int,input().split()))
# group = defaultdict(list)
# for i in range(n):
#     group["Group A"].append(input())
#     # print(group)
# for x in range(m):
#     group["Group B"].append(input())
#     # print(group)
# for i, word in enumerate(group["Group A"]):
#     group[word].append(i + 1)
# print(group)
