n = int(input())
arr = [int(input()) for _ in range(n)]
mn = arr[0]; mx = arr[0]; imin = 0; imax = 0
for i in range(1, n):
    if arr[i] < mn:
        mn, imin = arr[i], i
    if arr[i] > mx:
        mx, imax = arr[i], i
arr[imin], arr[imax] = arr[imax], arr[imin]
for x in arr:
    print(x, end=' ')
