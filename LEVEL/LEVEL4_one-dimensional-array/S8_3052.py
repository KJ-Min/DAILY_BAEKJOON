import sys

input = sys.stdin.readline

arr = []
for _ in range(10):
    N = int(input()) % 42
    arr.append(N)

arr2 = []
for i in range(10):
    if arr[i] not in arr2:
        arr2.append(arr[i])

print(len(arr2))
