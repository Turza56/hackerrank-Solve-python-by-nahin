if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    list1.sort(reverse=True)

    for i in range(n):
        if list1[i] > list1[i + 1] and list1[i] != list1[i + 1]:
            break

    print(list1[i + 1])
