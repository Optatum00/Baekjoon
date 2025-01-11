N, K = map(int, input().split())

queue = []
for i in range(1,N+1):
    queue.append(i)

res = [] # 결과값 저장
index = K-1 # 리스트 인덱스

while (len(queue) != 1):
    value = queue[index]
    queue.pop(index)
    res.append(value)
    index += K-1
    while (index > len(queue)-1):
        index = index - len(queue)

res.append(queue[0])
   
for i in range(len(res)):
    if (i == 0 and len(res) != 1):
        print('<'+str(res[i])+', ', end='')
    elif (i == 0 and len(res) == 1):
        print('<'+str(res[i])+'>')
    elif (i == len(res)-1):
        print(str(res[i])+'>', end='')
    else:
        print(str(res[i])+', ', end='')