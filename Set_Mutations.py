l = int(input())
ser = set(map(int,input().split()))
sum1 = 0
lis = []
range_of_code = int(input())
for _ in range(range_of_code):
    x = input().split()
    if x[0] == "intersection_update":
        inter_u = set(map(int,input().split()))
        ser.intersection_update(inter_u)
    elif x[0] == "update":
        sec_in =  set(map(int,input().split()))
        ser.update(sec_in)
    elif x[0] == "symmetric_difference_update":
        sym_diff_up =  set(map(int,input().split()))
        ser.symmetric_difference_update(sym_diff_up)
    elif x[0] == "difference_update":
        diff_up =  set(map(int,input().split()))
        ser.difference_update(diff_up)
for s in ser :
    lis.append(s)


for s in ser :
    sum1 = sum1 + int(s)
print(sum1)
