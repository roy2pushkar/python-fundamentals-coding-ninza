## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
row=1;
while row<=N:
  spaces =1
  while spaces<= N- row:
    print(" ",end="")
    spaces=spaces+1
  num=1
  while num<=row:
    print('*',end="")
    num=num+1;
  num=row-1

  while num>=1:
    print('*',end="")
    num=num-1
  print()
  row=row+14
