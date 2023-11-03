A = input()
B = input()
for i in range(len(B)):
    print(int(A) * int(B[-(i + 1)]))
print(int(A) * int(B))
