# Write your code here
bFlag = True
while bFlag:
    ch = int(input())
    if ch == 1:
        a = int(input())
        b = int(input())
        print(a + b)

    elif ch == 2:
        a = int(input())
        b = int(input())
        print(a - b)

    elif ch == 3:
        a = int(input())
        b = int(input())
        print(a * b)

    elif ch == 4:
        a = int(input())
        b = int(input())
        print(a // b)


    elif ch == 5:
        a = int(input())
        b = int(input())
        print(a % b)

    elif ch == 6:
        bFlag = False
        exit

    else:
        print("Invalid Operation")