import sys

num = []

def Palindrome(x):
    n = str(x)
    length = len(n)+1
    palindrome = ""
    for i in range(-1,-length,-1):
        palindrome += n[i]
    return int(palindrome)

while True:
    N = int(sys.stdin.readline().rstrip())
    if (N == 0):
        break
    num.append(N)

for i in num:
    if (Palindrome(i) == i):
        print("yes")
    else:
        print("no")