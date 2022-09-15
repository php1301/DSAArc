n = int(input())
a = list(map(int, input().split()))
i = 0
j = n - 1
eat = 1
while j != i:
  if(n<=2):
    break
  if(a[i] > a[j]):
    a[i]-=a[j]
    if(j-1 != i):
      j-=1
      eat+=1
    else:
      break
  elif(a[i] < a[j]):
    a[j]-=a[i]
    i+=1
  elif(a[i] == a[j]):
    i+=1
    if(j-1 != i):
      j-=1
      eat+=1
    else:
      break    
print(n-eat, eat)