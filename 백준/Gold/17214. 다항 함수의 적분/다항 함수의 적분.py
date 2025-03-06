import sys
import re
input = sys.stdin.readline

# 코드 좀 뒤엎어야함 인덱싱으로 숫자 걸러냈는데 생각해보니까 숫자가 한자리가 아니라 절댓값 10000까지 여서 다시 짜야함...
# 1000x+1000 이면 1000 1000 걸러내는 함수를 구현해야할듯
# case : x, -x, 10000, -10000, 10000x+10000, -10000x+10000, -10000x-10000

# 최대 일차 일변수 다항식 입력받기
polynomial = input().strip()
num = re.findall('\d+', polynomial)
if (len(num) == 2):
    if (num[1] == '0'):
        polynomial = polynomial[:2]
    if (num[1] == '1'):
        num[1] = ''
    if (num[1] == '-1'):
        num[1] = '-' 
if ('x' in polynomial):
    if (polynomial[0] == '-'):
        first_coefficient = str(int('-'+num[0])//2)
        if (first_coefficient == '-1'):
            first_coefficient = '-'
        if (polynomial.count('-') == 2):
            coefficient = '-'+num[1]
            print(first_coefficient+'xx'+coefficient+'x+W')
        elif ('+' in polynomial):
            coefficient = num[1]
            print(first_coefficient+'xx+'+coefficient+'x+W')
        else:
            print(first_coefficient+'xx+W')
    else:
        first_coefficient = str(int(num[0])//2)
        if (first_coefficient == '1'):
            first_coefficient = ''
        if ('-' in polynomial):
            coefficient = '-'+num[1]
            print(first_coefficient+'xx'+coefficient+'x+W')
        elif ('+' in polynomial):
            coefficient = num[1]
            print(first_coefficient+'xx+'+coefficient+'x+W')
        else:
            print(first_coefficient+'xx+W')
else:
    if (num[0] == '1'):
        num[0] = ''
    if (num[0] == '-1'):
        num[0] = '-'
    if ('-' in polynomial):
        coefficient = '-'+num[0]
        print(coefficient+'x+W')
    elif polynomial == '0':
        print('W')
    else:
        coefficient = num[0]
        print(coefficient+'x+W')