arrSize = list(map(int, input().split()))
arrPick = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


numFromArr1 = arr1[0:arrPick[0]][-1]
if arrPick[1] == len(arr2):
  numFromArr2 = arr2[0]
else:
	numFromArr2 = arr2[-arrPick[1]:][0]
if numFromArr1 < numFromArr2:
  print("YES")
else:
  print("NO")
  
