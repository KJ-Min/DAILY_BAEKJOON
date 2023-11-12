import sys

input = sys.stdin.readline

S = input().rstrip()

for i in range(97, 123):
    for j in range(len(S)):
        if S[j] == chr(i):
            print(j, end=" ")
            break
        elif j == len(S) - 1:
            print("-1", end=" ")
