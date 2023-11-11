import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    l = input().rstrip()
    print(f"{l[0]}{l[-1]}")
