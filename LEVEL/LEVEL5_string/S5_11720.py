import sys

input = sys.stdin.readline

N = int(input())

l = input().rstrip()

sum = 0

for i in range(N):
    sum = sum + int(l[i])
print(sum)
