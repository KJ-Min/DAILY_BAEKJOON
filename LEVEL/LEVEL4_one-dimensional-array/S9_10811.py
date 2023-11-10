import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(i + 1)

r_arr = []
for _ in range(M):
    i, j = map(int, input().split())
    for k in range(i - 1, j):
        r_arr.append(arr[k])
    r_arr.reverse()

    for l in range(j - i + 1):
        arr[(i - 1) + l] = r_arr[l]
    r_arr.clear()

for i in range(N):
    print(arr[i], end=" ")
