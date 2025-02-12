value1 = input()
value2 = input()
multi = input()

resistance =[['black',0],['brown',1],['red',2],['orange',3],['yellow',4],['green', 5],['blue', 6],['violet',7],['grey',8],['white',9]]

for i in resistance:
    if (i[0] == value1):
        first = str(i[1])
    if (i[0] == value2):
        second = str(i[1])
    if (i[0] == multi):
        third = 10**i[1]
print(int(first+second)*third)