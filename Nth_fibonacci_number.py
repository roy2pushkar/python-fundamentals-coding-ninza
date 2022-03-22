## Read input as specified in the question.
## Print output as specified in the question.
def fib(n):
    if n <= 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))