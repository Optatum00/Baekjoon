import sys

for i in range(3):
    x = sys.stdin.readline().strip()
    if (x.isdigit()):
        res = int(x) + (3-i)

def FizzBuzz(x):
    if (x%3==0 and x%5==0):
        return "FizzBuzz"
    elif (x%3==0 and x%5!=0):
        return "Fizz"
    elif (x%3!=0 and x%5==0):
        return "Buzz"
    else:
        return x

print(FizzBuzz(res))