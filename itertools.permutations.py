import itertoolsp1
n = input()
x= int(n[-1])

new_n = n.replace(n[-2:],'')
res = list(itertools.permutations(new_n, x))
new_res = sorted(res)
for item in new_res:
    print(''.join(item))