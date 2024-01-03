s = list(input())

cnt = 0

for i in range(len(s)):
    try:
        if (
            (s[i] == "l" and s[i + 1] == "j")
            or (s[i] == "c" and (s[i + 1] == "=" or s[i + 1] == "-"))
            or (s[i] == "d" and s[i + 1] == "-")
            or (s[i] == "n" and s[i + 1] == "j")
            or (s[i] == "s" and s[i + 1] == "=")
            or (s[i] == "z" and s[i + 1] == "=")
        ):
            cnt = cnt + 1
            s[i] = 0
            s[i + 1] = 0

        elif s[i] == "d" and s[i + 1] == "z" and s[i + 2] == "=":
            cnt = cnt + 1
            s[i] = 0
            s[i + 1] = 0
            s[i + 2] = 0
    except:
        break


for i in range(len(s)):
    if s[i] == "-" or s[i] == "=":
        s[i] = 0

for i in range(len(s)):
    if s[i] != 0:
        cnt = cnt + 1

print(cnt)
