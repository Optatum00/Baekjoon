import sys

num = []

def Palindrome(x):
    length = len(x)+1
    palindrome = ""
    for i in range(-1,-length,-1):
        palindrome += x[i]
    return palindrome

N = sys.stdin.readline().rstrip()
num.append(N)

for i in num:
    if (Palindrome(i) == i):
        print("1")
    else:
        print("0")
