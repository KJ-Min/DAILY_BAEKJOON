import sys

input = sys.stdin.readline

N, X = map(int, input().split())
N_list = list(map(int, input().split()))

for i in range(N):
    if N_list[i] < X:
        print(N_list[i], end=" ")
