S = input()
if len(S) == 1:
    print(1)
else:
    for i in range(len(S) // 2):
        if len(S) % 2 == 0:
            if S[len(S) // 2 - 1 - i] != S[len(S) // 2 - 1 - i + (2 * (i + 1) - 1)]:
                print(0)
                break
            elif i == len(S) // 2 - 1:
                print(1)
        else:
            if S[len(S) // 2 - 1 - i] != S[len(S) // 2 - 1 - i + (2 * (i + 1))]:
                print(0)
                break
            elif i == len(S) // 2 - 1:
                print(1)

# 6 > 3
# 7 > 3
# 8 > 4
# 9 > 4

# 012

# 35 > 24 > 2
# 26 > 15 > 4
# 17 > 06 > 6
