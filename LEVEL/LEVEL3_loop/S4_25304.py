X = int(input())
N = int(input())
alist = []

for _ in range(N):
    a, b = map(int, input().split())
    alist.append([a, b])

sum = 0
for blist in alist:
    sum = sum + (blist[0] * blist[1])

if X == sum:
    print("Yes")
else:
    print("No")
