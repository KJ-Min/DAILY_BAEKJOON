import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] * N
for _ in range(M):
    A, B, C = map(int, input().split())
    for j in range(A - 1, B):
        arr[j] = C

for i in range(N):
    print(arr[i], end=" ")
