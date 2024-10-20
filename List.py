if __name__ == '__main__':
    N = int(input())
    ls =[]
    for _ in range(N):
        command = str(input()).split()
        if "append" == command[0]:
            ls.append(int(command[1]))

        elif "insert" == command[0]:
            ls.insert(int(command[1]),int(command[2]))

        elif  "remove" == command[0]:
            ls.remove(int(command[1]))

        elif  "reverse" == command[0]:
            ls.reverse()

        elif  "sort" == command[0]:
            ls.sort()

        elif  "pop" == command[0]:
            ls.pop()

        elif  "print" == command[0]:
            print(ls)