if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    allx = [i for i in range(x+ 1)]
    ally = [i for i in range(y+ 1)]
    allz = [i for i in range(z+ 1)]
    nm = [[a,b,c] for a in allx for b in ally for c in allz]

    print([x for x in nm if sum(x) != n])
