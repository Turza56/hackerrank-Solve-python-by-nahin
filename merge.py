def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sep = string[i:i + k]
        mer = set(sep)
        print(''.join(mer))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)