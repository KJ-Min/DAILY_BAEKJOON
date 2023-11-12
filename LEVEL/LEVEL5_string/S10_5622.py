alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "22233344455566677778889999"

S = input()
arr = []

for i in S:
    for j in range(len(alpha)):
        if i == alpha[j]:
            arr.append(int(num[j]) + 1)
            break
print(sum(arr))
