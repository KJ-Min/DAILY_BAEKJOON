A, B, C = map(int, input().split())
if A == B == C:
    print(f"{10000+(1000*A)}")
elif A != B != C and A != C != B:
    print(f"{max(A,B,C)*100}")
else:
    if A == B:
        print(f"{1000+(100*A)}")
    elif B == C:
        print(f"{1000+(100*B)}")
    else:
        print(f"{1000+(100*A)}")
