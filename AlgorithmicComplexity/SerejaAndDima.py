n = int(input())
a = list(map(int, input().split()))

i, j = 0, n - 1
count = 0
sumS = 0
sumD = 0
while i != j and i < n and j < n:
  if count % 2 == 0:
    if(a[i] > a[j]):
      sumS+=a[i]
      i+=1
    else:
      sumS+=a[j]
      j-=1
  else:
    if(a[i] > a[j]):
      sumD+=a[i]
      i+=1
    else:
      sumD+=a[j]
      j-=1
  count+=1   
if(count % 2 == 0):
  sumS+=a[i]
else:
  sumD+=a[i]
print(sumS, sumD)