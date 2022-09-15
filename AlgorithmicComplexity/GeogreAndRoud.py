n, k = map(int, input().split()) 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

avail = set([])
startIndex = 0
for i in range(0, len(arr2)):
    if arr2[i] >= arr1[0]:
      startIndex = i
      break
if(arr2[startIndex] >= arr1[0]):
  i = 0
  while startIndex < len(arr2):
    if(arr2[startIndex] == arr1[i]):
      startIndex+=1
    else:
      avail.add(arr1[i])
      i+=1
      startIndex+=1
print(avail)
print(len(avail))