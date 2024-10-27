r, c = input().split()
lis = list()
for _ in range(int(c)):
    sub = map(float,input().split())
    lis.append(sub)
for i in zip(*lis):
    print(sum(i)/len(i))
