N = int(input())
K = input()
even_cnt = 0
odd_cnt = 0

K_list = list(K)
for i in range(len(K_list)):
    test = int(K_list[i])
    if test % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

if even_cnt > odd_cnt:
    print("0")
elif even_cnt == odd_cnt:
    print("-1")
else:
    print("1")