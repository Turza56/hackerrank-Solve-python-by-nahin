l = int(input())
ser1 = list(map(int,input().split()))
ser = set(ser1)
sum1 = 0
lis = []
range_of_code = int(input())
for _ in range(range_of_code):
    x = input().split()
    if x[0] == "intersection_update":
        inter_u = map(int,input().split())
        ser.intersection_update(inter_u)
    elif x[0] == "update":
        sec_in = list(input().split())
        ser.update(sec_in)
    elif x[0] == "symmetric_difference_update":
        sym_diff_up = list(input().split())
        ser.symmetric_difference_update(sym_diff_up)
    elif x[0] == "differcence_update":
        diff_up = list(input().split())
        ser.difference_update(diff_up)
for s in ser :
    lis.append(s)


for ss in lis :
    sum1 = sum1 + int(ss)
print(sum1)
