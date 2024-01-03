N = int(input())
cnt = 0


def check(word):
    index = []
    for i in range(len(word)):
        spell = word[i]
        for j in range(len(word)):
            if word[j] == spell:
                index.append(j)
        if len(index) == 1:
            index = []
            continue
        else:
            for k in range(len(index) - 1):
                if index[k] - index[k + 1] == -1:
                    continue
                else:
                    return False
            index = []
    return True


for _ in range(N):
    word = input()

    chk = check(word)
    if chk == True:
        cnt += 1
    else:
        None

print(cnt)
