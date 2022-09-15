n = int(input())
arr = list(map(int, input().split()))
i = 0
j = 0
maxI = minI = arr[0]
length = 0

while j < n:
  while j < n and abs(arr[j] - minI) <= 1 and abs(arr[j] - maxI) <= 1:
    if arr[j] > maxI:
      maxI = arr[j]
    if arr[j] < minI:
      minI = arr[j]
    j+=1  
  length = max(length, j - i)
  if j < n and arr[j] > maxI:
    minI = maxI
  if j < n and arr[j] < minI:
    maxI = minI
  for idx in range (j - 1, i-1, -1):
    if arr[idx] != arr[j-1]:
      i = idx+1
      break
  
    
print(length)
