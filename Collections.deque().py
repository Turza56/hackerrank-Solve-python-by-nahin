from collections import deque
d = deque()
n = int(input())
for i in range(n):
    x = input().split()
    if x[0] == "append":
        d.append(x[-1])
    elif x[0] == "appendleft":
        d.appendleft(x[-1])
    elif x[0] == "pop":
        d.pop()
    elif x[0] == "popleft":
        d.popleft()

print(" ".join(d))
