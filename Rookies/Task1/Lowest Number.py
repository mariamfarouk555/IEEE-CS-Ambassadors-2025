n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
min_value = arr[0]
min_pos = 1  
for i in range(1, n):
    if arr[i] < min_value:
        min_value = arr[i]
        min_pos = i + 1  
print(min_value, min_pos)
