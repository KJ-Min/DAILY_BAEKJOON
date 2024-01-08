import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = []
S = []
temp = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        temp.append(A[i][j] + B[i][j])
    S.append(temp)
    temp = []

for i in range(N):
    for j in range(M):
        print(S[i][j], end=" ")
    print()
