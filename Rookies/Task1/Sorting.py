n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
for num in arr:
    print(num, end=' ')
