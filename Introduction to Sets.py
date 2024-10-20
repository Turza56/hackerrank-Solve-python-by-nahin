def average(array):
   sum = 0
   x = set(array)
   size = len(x)
   for i in x :
       sum = sum + i

   return sum/size

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)