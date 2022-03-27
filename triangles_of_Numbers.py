## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n - i:
        print(' ', end='')
        s = s + 1
    num = 1
    p = i
    while num <= i:
        print(p, end='')
        num = num + 1
        p = p + 1
    p = i - 1

    while p >= 1:
        print(p + i - 1, end='')
        p = p - 1

    print()
    i = i + 1