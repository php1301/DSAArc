s = input()
t = input()
n = 0

arrSumS = list(s)
arrSumT = list(t)

flag = 0
finalStr = ''

if len(arrSumS) == len(arrSumT):
  if(sorted(arrSumS) == sorted(arrSumT)):
    print('array')
  else:
    print('need tree')
else:
  if(s.find(t)!= -1):
    print('automaton')
  else:
    for idx in range(0, len(arrSumS)):
      if(idx < len(t)):
        if arrSumS[idx] != arrSumT[n]:
          arrSumS[idx] = '0'
        else:
          n+=1
    while '0' in arrSumS: 
      arrSumS.remove('0')
    finalStr = ''.join(map(str, arrSumS))
    if(finalStr == t):
      print('automaton')
    else:
      for idx in range(0, len(t)):
        if t[idx] not in s:
          print('need tree')
          flag = 1
          break
        else:
          idx = s.index(t[idx])
          s = s[:idx] + '0' + s[idx + 1:]
      if flag == 0:
        print('both')