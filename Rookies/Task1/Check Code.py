a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])
s = input().strip()
valid = True
if len(s) != a + b + 1:
    valid = False
else:
    if s[a] != '-':
        valid = False
    else:
        for i in range(len(s)):
            if i == a:
                continue
            ch = s[i]
            if ch < '0' or ch > '9':
                valid = False
                break
print("Yes" if valid else "No")
