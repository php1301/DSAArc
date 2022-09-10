s = input()
t = input()
strRes = ''
lenStr = len(s)
flag = 1
for i in range(0, lenStr):
  val = abs(ord(s[i]) - ord(t[i]))
  strRes += s[i]
  if val != 0:
    flag = 0
    

if flag == 0:
  strRes = strRes[:-1]
  if chr(ord(s[-1])) == 'z':
    strRes = t
    strRes = strRes[:-1]
    strRes += 'a'
  else:
  	strRes += chr(ord(s[-1])+1)
  if strRes != t:
  	print(strRes)
  else:
    print('No such string')
else:
  print('No such string')