import sys

input = sys.stdin.readline

while 1:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
