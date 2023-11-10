import sys

input = sys.stdin.readline

arr = [0] * 30

for _ in range(28):
    n = int(input())
    arr[n - 1] = n

for i in range(30):
    if arr[i] == 0:
        print(i + 1)
