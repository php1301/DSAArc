n, k = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
max_book = 0
i = 0
for idx in range(n) :
  sum+=arr[idx]
  while sum > k:
    sum-=arr[i]
    i+=1
  max_book = max(max_book, idx - i)
if max_book == 0:
  if arr[max_book] > k:
    print('0')
  else:
    print(max_book + 1)
else:
  print(max_book + 1)    