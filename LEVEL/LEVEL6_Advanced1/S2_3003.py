import sys

input = sys.stdin.readline

pieces = list(map(int, input().split()))

board = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(len(board)):
    if pieces[i] == board[i]:
        answer.append(0)
    else:
        answer.append(board[i] - pieces[i])

for i in range(len(answer)):
    print(answer[i], end=" ")
