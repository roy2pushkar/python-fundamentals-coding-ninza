## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a = n - (n // 2 + 1)
b = n - a
i = 1
while i <= b:
    j = 1
    while j <= i - 1:
        print(' ', end='')
        j = j + 1
    j = 1
    while j <= i:
        print('* ', end='')
        j = j + 1
    print()
    i = i + 1
i = a
while i >= 1:
    j = 1
    while j <= i - 1:
        print(' ', end='')
        j = j + 1
    k = 1
    while k <= i:
        print('* ', end='')
        k = k + 1

    print()
    i = i - 1