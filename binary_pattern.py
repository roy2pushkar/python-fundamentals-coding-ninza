## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1):
  for k in range(1,n-i+2):
    if i%2==0:
      print(0,end="")
    else:
      print(1,end="")
  print()