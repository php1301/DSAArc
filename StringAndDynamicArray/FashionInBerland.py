n = int(input())
arr = list(map(int, input().split()))
if len(arr) == 1:
    if arr[0] == 0:
        print('NO')
    else:
        print('YES')
else:
    count = 0
    for x in arr:
        if x == 0:
            count += 1

    if count == 1:
        print('YES')
    else:
        print('NO')
