import sys

N = int(sys.stdin.readline().rstrip())
Size_lst = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

T_bundle, P_bundle, P_each = 0, 0, 0

for size in Size_lst:
    if (size == 0):
        continue    
    elif (size <= T):
        T_bundle += 1
    else:
        if (size%T == 0):
            T_bundle += (size//T)
        else:
            T_bundle += (size//T)+1

P_bundle = N//P
P_each = N%P

print(T_bundle)
print(P_bundle, P_each)