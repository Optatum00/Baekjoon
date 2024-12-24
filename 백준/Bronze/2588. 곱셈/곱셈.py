a = int(input())
b = list(map(int,input()))
sum_3 = a*b[2]
sum_4 = a*b[1]
sum_5 = a*b[0]
sum_total = sum_5*100+sum_4*10+sum_3
print(sum_3,"\n",sum_4,"\n",sum_5,"\n",sum_total,"\n",sep='')