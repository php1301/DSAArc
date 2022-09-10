n = int(input())
arr = list(map(int, input().split()))
arr.append(90)
start = 0
res = 0
for num in arr:
  if num - start <= 15:
    res += int(num-start)
    start = num
  else:
    res += 15
    break
    
print(res)
  