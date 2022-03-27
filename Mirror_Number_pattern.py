## Read input as specified in the question
## Print the required output in given format
N = int(input())
row = 1;
while row <= N:
    spaces = 1
    while spaces <= N - row:
        print(" ", end="")
        spaces = spaces + 1
    num = 1
    while num <= row:
        print(num, end="")
        num = num + 1;
    num = row - 1

    print()
    row = row + 14
