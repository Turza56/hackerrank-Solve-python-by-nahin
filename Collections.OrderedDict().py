from collections import OrderedDict
N = int(input())
ordered_dictionary = OrderedDict()
for _ in range(N):
    x = input().split()
    item_name = " ".join(x[:-1])
    net_price = int(x[-1])
    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] = ordered_dictionary[item_name] + net_price
    else:
        ordered_dictionary[item_name] = net_price
for item_name, net_price in ordered_dictionary.items():
    print(item_name, net_price)
