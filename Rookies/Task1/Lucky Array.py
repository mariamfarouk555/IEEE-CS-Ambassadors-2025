n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
mn = arr[0]
for x in arr[1:]:
    if x < mn:
        mn = x
cnt = 0
for x in arr:
    if x == mn:
        cnt += 1
print("Lucky" if cnt % 2 == 1 else "Unlucky")
