n = int(input())
s = set(map(int, input().split()))

a = int(input())
sum = 0
for _ in range(a):
    x = (input().split())
    if x[0] == "remove":
        s.remove(int(x[1]))

    elif x[0] == "pop":
        s.pop()

    elif x[0] == "discard":
        s.discard(int(x[1]))

for s1 in s:
    sum = sum + s1
print(sum)
