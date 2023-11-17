N = int(input())

for i in range(N):
    print(str("*" * (2 * (i + 1) - 1)).rjust(N + i))

for i in range(N - 1):
    print(str("*" * (2 * (N - 1 - i) - 1)).rjust(2 * N - 1 - (i + 1)))
