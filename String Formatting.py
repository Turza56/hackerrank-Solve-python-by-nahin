
def print_formatted(number):
        for i in range(1, number + 1):
            x = len(bin(number)) - 2
            print(f"{i :>{x}}",
                  f"{oct(i)[2:]:>{x}}",
                  f"{hex(i).upper()[2:]:>{x}}",
                  f"{bin(i)[2:]:>{x}}")

if __name__ == '__main__':
    n = int(17)
    print_formatted(n)





"""
bin_width = len(bin(number)) - 2
return f"{number:>{bin_width}} {oct(number)[2:]:>{bin_width}} {hex(number)[2:]:>{bin_width}} {bin(number)[2:]:>{bin_width}}"

   """
