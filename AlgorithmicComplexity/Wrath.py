n = int(input())
arr = list(map(int, input().split()))

alive = 0
startKilledIdx = n
for idx in range(n-1, -1, -1):
  
  if(idx < startKilledIdx):
    alive+=1
  startKilledIdx = min(startKilledIdx, idx - arr[idx])

print(alive)   