H, M = map(int, input().split())
if M >= 45:
    M = M - 45
    print(f"{H} {M}")
else:
    if H == 0:
        print(f"{23} {M+60-45}")
    else:
        print(f"{H-1} {M+60-45}")
