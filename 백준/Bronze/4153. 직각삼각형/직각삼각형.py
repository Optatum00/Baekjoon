while(True):
    test = list(map(int, input().split()))
    if (test[0] == test[1] == test[2] == 0):
        break
    max = max(test)
    test.remove(max)
    if(max**2 == test[0]**2 + test[1]**2):
        print('right')
        del max
    else:
        print('wrong')
        del max