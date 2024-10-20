input_num = int(input())
country_set = set()
for x in range(input_num):
    country_nam = input()
    country_set.add(country_nam)
print(len(country_set))
