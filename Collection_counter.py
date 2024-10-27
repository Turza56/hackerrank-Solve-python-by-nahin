from collections import Counter
shoe_available = int(input())
x = map(int, input().split())
shoe_size = list(x)
shoe_counter = Counter(shoe_size)
shoe_key = shoe_counter.keys()
shoe_value = shoe_counter.values()

customer_num = int(input())
customer = []
add = []
total = 0
for i in range(customer_num):
        sell = list(map(int, input().split()))
        customer.append(sell)

for z in range(len(customer)):
        if shoe_counter[customer[z][0]] > 0 :
            shoe_counter[customer[z][0]] -= 1
            add.append(customer[z][-1])
            print("Customer",z+1,": Purchased size", customer[z][0],"shoe for $"+ str(customer[z][-1]) +".")
        else:
            print("Customer",z+1,": Size", customer[z][0] ,"not available, so no purchase.")
for m in add:
        total = total + m
print(total)