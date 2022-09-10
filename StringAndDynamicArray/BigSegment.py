n = int(input())
segList = []
minValInSeg, maxValInSeg = 0, 0
for seg in range(0, n):
  numSegments = list(map(int, input().split()))
  if numSegments[1] > maxValInSeg:
    maxValInSeg = numSegments[1]
  if minValInSeg == 0 or numSegments[0] < minValInSeg:
    minValInSeg = numSegments[0]
  segList.append(numSegments)

segToFind = str(minValInSeg) + '-' + str(maxValInSeg)

flag = 0
for i in range(0, len(segList)):
  currentStrList = '-'.join(map(str, segList[i]))
  if currentStrList == segToFind:
    print(i + 1)
    flag = 1
    break
    
if flag == 0:
  print('-1')

