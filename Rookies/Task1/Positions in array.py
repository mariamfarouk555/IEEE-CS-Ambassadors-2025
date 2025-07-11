n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
for i in range(n):
    if arr[i] <= 10:
        print(f"A[{i}] = {arr[i]}")
