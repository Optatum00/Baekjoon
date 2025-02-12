import sys
input = sys.stdin.readline
T = int(input().strip())
# logic 정리
# alphabet 리스트가 있음 -> 입력한 단어를 한단어씩 분석 -> [첫단어가 if a 다음단어 a인지 계속 체크 -> 끝나면 리스트에서 지움]
# 근데 만약 다시 나오면 groupword 아님 이 방식으로 단어 끝까지 통과시 groupword 맞음.

def groupword_checker(S):
    aList = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(len(S)):
        if (i == 0):
            if (S[i] in aList):
                pre = S[i]
        else:
            if (pre == S[i]):
                continue
            else:
                if (S[i] in aList):
                    aList.remove(pre)
                    pre = S[i]
                else:
                    return False
    return True
count = 0
for i in range(T):
    word = input().strip()
    if groupword_checker(word):
        count += 1
print(count)