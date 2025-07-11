n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
is_palindrome = True
for i in range(n // 2):
    if arr[i] != arr[n - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print("YES")
else:
    print("NO")
