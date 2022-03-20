## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
a=input()
b=list(map(int,a))
even=0
odd=0
for i in range(0,len(b)):
    if b[i]%2 ==0:
        even=even+b[i]
    else:
        odd=odd+b[i]
print(even,odd)