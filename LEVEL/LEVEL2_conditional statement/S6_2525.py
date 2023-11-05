A, B = map(int, input().split())
C = int(input())
CD = C // 60
CR = C % 60
A = A + CD
B = B + CR

if B >= 60:
    A = A + 1
    B = B - 60

if A >= 24:
    A = A % 24

print(f"{A} {B}")
