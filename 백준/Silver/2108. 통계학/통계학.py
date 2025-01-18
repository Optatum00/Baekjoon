import sys
N = int(sys.stdin.readline().strip())

# python round()는 오사오입방식임 round(2.5) -> 2 따라서 실질적인 반올림 구현 필요해서 구현
def custom_round(num):
    if (num < 0):
        num = abs(num)
        num = custom_round(num)
        return int('-'+str(num))
    else:
        if ((num - int(num)) >= 0.5):
            return int(num)+1
        else:
            return int(num)

v_list = []
dict = {}

for i in range(N):
    value = int(sys.stdin.readline().strip())
    v_list.append(value)

def mean(x):
    count = 0
    for i in x:
        count += i
    return custom_round(count/len(x))

def median(x):
    x.sort()
    return x[(len(x)//2)]

def mode(x):
    a = {}
    res = []
    for i in x:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    max_num = max(a.values())
    for key in a.keys():
        if ( a[key] == max_num):
            res.append(key)
    res.sort()
    if (len(res) == 1):
        return res[0]
    else:
        return res[1]

def extent(x):
    return max(x) - min(x)

print(mean(v_list))
print(median(v_list))
print(mode(v_list))
print(extent(v_list))