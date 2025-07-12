n = int(input())
digits = input().strip()
while len(digits) != n:
    print("Error: enter exactly", n, "digits")
    digits = input().strip()
total = 0
for ch in digits:
    total += int(ch)
print(total)
