n = list(map(int, input().split()))
arrPass = []
for _ in range(0, n[0]):
    val = input()
    arrPass.append(val)
password = input()

sumWorst = 0
sumBest = 1
countResetBest = 0
numFail = 0
for p in arrPass:
  if len(p) <= len(password):
    if len(p) != len(password):
        sumBest += 1
        countResetBest += 1
        if countResetBest % n[1] == 0:
            sumBest += 5

for p in arrPass:
  if len(p) <= len(password):
        if p != password and len(p) == len(password):
            sumWorst += 1
            countResetBest += 1
            if countResetBest % n[1] == 0:
          	  sumWorst += 5
print(sumBest, sumWorst + sumBest)
