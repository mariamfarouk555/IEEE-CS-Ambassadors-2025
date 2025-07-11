n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
for i in range(n):
    if arr[i] > 0:
        arr[i] = 1
    elif arr[i] < 0:
        arr[i] = 2
    else:
        arr[i]=0
for num in arr:
    print(num, end=" ")
