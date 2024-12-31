N, M = map(int, input().split())

if (M <= 26):
    ob = chr(M+64)
elif (26<M<=702):
    F = M//26
    B = M%26
    if (B == 0):
        B = 26
        F -= 1
    ob = chr(F+96) + chr(B+96)

result = "SN " + str(N) + ob
print(result)