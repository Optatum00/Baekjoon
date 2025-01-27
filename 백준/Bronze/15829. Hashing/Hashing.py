import sys
L = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

def hashing(L):
    sum, r, M = 0, 31, 1234567891
    for i in range(L):
        sum += (ord(S[i])-96)*r**i
    return sum%M

print(hashing(L))