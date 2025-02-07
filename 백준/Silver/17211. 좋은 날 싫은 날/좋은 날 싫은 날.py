N, weather = map(int, input().split())
goodday = 0
badday = 0

def custom_round(n):
    if (n-int(n) >= 0.5):
        return int(n)+1
    else:
        return int(n)
    
gg, gb, bg, bb = map(float, input().split())

if weather == 1:
    g,b = 0,1
else:
    g,b = 1,0

for i in range(N):
    goodday = g*gg+ b*bg
    badday = b*bb + g*gb
    g = goodday
    b = badday

print(custom_round(goodday*1000))
print(custom_round(badday*1000))