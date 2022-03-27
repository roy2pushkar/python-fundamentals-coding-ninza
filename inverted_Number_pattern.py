## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = n
while i >= 1:
    j = 1
    while j <= i:
        print(i, end='')
        j = j + 1
    print()
    i = i - 1

