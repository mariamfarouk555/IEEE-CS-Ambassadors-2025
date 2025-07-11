n = int(input("Enter how many numbers: "))
arr = []
for _ in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)
result = sum(x for x in arr)

print("Absolute sum:",abs(result))
