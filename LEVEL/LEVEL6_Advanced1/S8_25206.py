import sys

input = sys.stdin.readline
score_chart = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

tot_score = []
tot_credits = []

for _ in range(20):
    course, credit, grade = map(str, input().split())
    if grade != "P":
        score = score_chart[grade] * float(credit)
        tot_score.append(score)
        tot_credits.append(float(credit))

print(sum(tot_score) / sum(tot_credits))
