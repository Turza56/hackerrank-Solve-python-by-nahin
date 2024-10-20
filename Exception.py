x = int(input())
numbers = []
for i in range(x):
    try:

        a, b = list(map(int, input().split()))
        z = a//b
        numbers.append(z)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    # except ValueError:
    #     print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print(f"Error Code: {e}")

for number in numbers:
    print(number)
