if __name__ == '__main__':
    s = input()
    print(s)

    if s.isalnum():
        print(True)
    else:
        if any(char.isalpha() for char in s):
            print(True)
        else:
            print(False)

    if  s.isalpha() :
        print(True)
    elif s.isalnum() and not s.isdigit():
        print(True)
    elif not s.isalnum():
        if s.isdigit():
            print(False)
        else:
            if all(not char.isalnum() for char in s):
                print(False)
            else:
                if any(char.isalpha() for char in s):
                    print(True)
                else:
                    print(False)
    else:
        print(False)

    if s.isdigit():
        print(True)
    elif s.isalnum() and not s.isalpha():
        print(True)
    elif not s.isalnum():
        if s.isalpha():
            print(False)
        else:
            if all(not char.isalnum() for char in s):
                print(False)
            else:
                if any(char.isdigit() for char in s):
                    print(True)
                else:
                    print(False)
    else:
        print(False)

    if not s.isdigit() and not s.isupper():
        if all(not char.isalnum() for char in s):
            print(False)
        else:
            if any(char.islower() for char in s):
                print(True)
            else:
                print(False)

    else:
        print(False)

    if not s.isdigit() and not s.islower():
        if all(not char.isalnum() for char in s):
            print(False)
        else:
            if any(char.isupper() for char in s):
                print(True)
            else:
                print(False)

    else:
        print(False)



