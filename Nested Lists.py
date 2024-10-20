if __name__ == '__main__':
    list1 = []

    n=int(input())
    for i in range(0,n ):
        name = input()
        score = float(input())

        ele = [name, score]
        list1.append(ele)
        list1.sort()

    # print(list1)

    minElement = 0
    for x in range(len(list1)) :
       if x == 0 :
          min = list1[x][1]
       else:
          if list1[x][1] <= min:
             min = list1[x][1]
             minElement = list1[x]
    print(min)

    # list1.remove(minElement)
    list2 = list(filter(lambda y: y[1] != min, list1))
    print(list2)


    for x in range(len(list2)) :
       if x == 0 :
          min = list2[x][1]
       else:
          if list2[x][1] <= min:
             min = list2[x][1]
             minElement = list2[x]
    print(min)

    list3= list(filter(lambda  y : y[1] == min, list1))
    for i in range(len(list3)):
       print(''.join(list3[i][0]))







    # print(''.join(list1[x+1][0]))
    # print(''.join(list1[x][0]))



