croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=']
S = input()
count, S_count = 0, 0

if ('dz=' in S):
    if (S.count('dz=') == S.count('z=')): # dz=만 있는 경우
        count += S.count('dz=')
        S_count += 3*S.count('dz=')
    else: # dz= z= 둘다 있는 경우
        num_dz = S.count('dz=')
        num_z = S.count('z=') - num_dz
        count += (num_dz + num_z)
        S_count += (3*num_dz+2*num_z)
else:
    if ('z=' in S):
        count += S.count('z=')
        S_count += 2*S.count('z=')

for i in croatia:
    if(i in S):
        x = S.count(i)
        count += x
        S_count += len(i)*x
count += (len(S) - S_count)
print(count)