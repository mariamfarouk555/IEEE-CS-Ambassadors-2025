T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        num = int(input())
        arr.append(num)
    result = []
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]
            result.append(max(subarray))
    for value in result:
        print(value, end=" ")
    print()
