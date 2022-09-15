n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j = 0, 0
arrRes = []
while j < m and i < n:
  minVest = a[i] - x
  if a[i]-x < 0:
    minVest = 0
  maxVest = a[i] + y
  if b[j] > maxVest:
    i+=1
  elif b[j] < minVest:
    j+=1
  elif b[j] >= minVest and b[j] <= maxVest:
    arrRes.append([i+1, j+1])
    i+=1
    j+=1
print(len(arrRes))
for idx in range(len(arrRes)):
  print(str(arrRes[idx][0]) + ' ' + str(arrRes[idx][1]))