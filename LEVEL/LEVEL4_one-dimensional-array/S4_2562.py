import sys

input = sys.stdin.readline
arr = []

for _ in range(9):
    arr.append(int(input()))

for i in range(9):
    if arr[i] == max(arr):
        print(arr[i])
        print(i + 1)
