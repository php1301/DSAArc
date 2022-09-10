str = input()
sum = 0
start = 'a'
for i in range(0, len(str)):
  indexOfWord = abs(ord(str[i]) - ord(start))
  counterRange = 26 - indexOfWord
  sum += min(counterRange, indexOfWord)
  start = str[i]
print(sum)