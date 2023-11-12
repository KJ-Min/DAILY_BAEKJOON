import sys

input = sys.stdin.readline

T = int(input())
line = ""
for i in range(T):
    R, S = input().split()
    for j in range(len(S)):
        line = line + S[j] * int(R)
    print(line)
    line = ""
