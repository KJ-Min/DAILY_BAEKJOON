S = list(input().upper())

num = []
cnt = 0
for i in set(S):
    for j in range(len(S)):
        if i == S[j]:
            cnt = cnt + 1
    num.append(cnt)
    cnt = 0

ans = []
for i in range(len(num)):
    if num[i] == max(num):
        ans.append(list(set(S))[i])

if len(ans) != 1:
    print("?")
else:
    print(ans[0])
