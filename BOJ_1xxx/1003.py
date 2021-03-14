# 피보나치함수
m_0=[1,0]
m_1=[0,1]
for i in range(int(input())):
    a=int(input())
    for j in range(a):
        m_0.append(m_0[j]+m_0[j+1])
        m_1.append(m_1[j]+m_1[j+1])
    print(m_0[a],m_1[a])
    m_0=[1,0]
    m_1=[0,1]
