import sys

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

A = arr[0][0]
B = [0, 0]

for i in range(9):
    for j in range(9):
        if A < arr[i][j]:
            A = arr[i][j]
            B = [i, j]
print(A)
print(B[0] + 1, B[1] + 1)
