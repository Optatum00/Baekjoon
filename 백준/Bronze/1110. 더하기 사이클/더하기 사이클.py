N = input()
target = int(N)
count = 0

if (len(N) <2):
    N = '0'+N

while (True):
   N = N[1] + str(int(N[0])+int(N[1]))[-1]
   count += 1
   if (int(N) == target):
       break

print(count)