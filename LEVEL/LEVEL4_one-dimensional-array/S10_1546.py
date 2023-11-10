import sys

input = sys.stdin.readline
N = int(input())
grade = list(map(int, input().split()))

max_grade = max(grade)
avg = [i / max_grade * 100 for i in grade]

print(sum(avg) / N)
