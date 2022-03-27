## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    j=1
    k=1
    while k<=n-i:
         print(' ',end='')
         k=k+1
    p=i
    while j<=i:
        print(p,end='')
        j=j+1
        p=p-1
    j=1
    p=2
    while j<=i-1:
        print(p,end='')
        j=j+1
        p=p+1
    print()
    i=i+1