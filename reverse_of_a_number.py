#Write Your Code Here
n = int(input())
rev = 0
rem = 0
while(n != 0):
    rem = n%10
    rev = rev*10 +rem
    n = int(n/10)
print(rev)
