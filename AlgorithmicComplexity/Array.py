n, k = map(int, input().split()) 
arr = list(map(int, input().split()))
l, r = -1, -1
if k == 1:
    print (1, 1)
arrShowed = set([])
temp = set([])
for i in range(n):
    if l != -1:
        arrShowed.add(arr[i])
    elif l == -1 and arr[i] != arr[0]:
        l = i
        arrShowed.add(arr[0])
        arrShowed.add(arr[i])
    if len(arrShowed) == k:
        r = i + 1
        break
if l != -1 and r != -1:
    for i in range(r - 1, l - 2, -1):
        temp.add(arr[i])
        if len(temp) == k:
            l = i + 1
            break
    print (l, r)
else:
    print (-1, -1)