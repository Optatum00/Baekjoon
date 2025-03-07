import sys
from math import *
input = sys.stdin.readline
# 한줄평 : 중고등학교 기하 개념 중요하다. 필요한 개념 : 합동, 코사인법칙, 삼각형넓이 - 1/2*a*b*cosc, 부채꼴 넓이 : 1/2*r^2*x(부채꼴 각도)
# 입력 받기
x1, y1, r1, x2, y2, r2 = map(float, input().strip().split())
d = sqrt((x1-x2)**2+(y1-y2)**2)
# 주어지는 원 판단 (1. 두 원이 겹치지 않음 2. 한 원이 다른원에 완전히 들어감 3. 두 원이 일부분 겹침)

if (d >= r1+r2):
    print('0.000')
elif(d <= abs(r1-r2)):
    print(round(min(r1,r2)**2*pi,3))
else:
    theta1 = 2*acos((r1**2+d**2-r2**2)/(2*r1*d))
    theta2 = 2*acos((r2**2+d**2-r1**2)/(2*r2*d))
    S = round(1/2*r1**2*(theta1-sin(theta1))+1/2*r2**2*(theta2-sin(theta2)), 3)
    print(S)