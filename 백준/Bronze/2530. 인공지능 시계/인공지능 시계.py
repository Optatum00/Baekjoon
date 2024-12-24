h_now, m_now, s_now = map(int, input().split())
t = int(input())

if t>=3600:
    h = t//3600
    if t%3600 >= 60:   
        m = (t%3600)//60
        s = (t%3600)%60
    else:
        m = 0
        s = t%3600
else:
    h = 0
    m = t//60
    s = t%60

s_final = s_now + s
m_final = m_now + m
h_final = h_now + h
    
if s_final>=60:
    m_final = m_final + s_final//60
    s_final = s_final%60
    
if m_final>=60:
    h_final = h_final + m_final//60
    m_final = m_final%60
    
if h_final>23:
    if h_final == 24:
        h_final = 0
    else:
        h_final = h_final%24

print(h_final, m_final, s_final)