fee = int(input())
remain = 1000 - fee

coin = [500, 100, 50, 10, 5, 1]
cnt = 0


for i in range(len(coin)):
    if remain // coin[i] >= 1:
        share = remain // coin[i]
        cnt += share
        remain = remain - coin[i] * share

print(cnt)
