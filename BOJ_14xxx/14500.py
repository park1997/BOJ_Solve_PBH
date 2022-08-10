# 테트로노미노
import sys
N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
s1 = [[0,0],[1,0],[1,1],[2,1]]
s2 = [[0,0],[1,0],[1,-1],[2,-1]]
s3 = [[0,0],[0,1],[0,2],[0,3]]
s4 = [[0,0],[1,0],[2,0],[3,0]]
s5 = [[0,0],[1,0],[2,0],[2,1]]
s6 = [[0,0],[1,0],[1,-1],[1,-2]]
s7 = [[0,0],[0,1],[1,1],[2,1]]
s8 = [[0,0],[0,-1],[1,-1],[2,-1]]
s9 = [[0,0],[1,-1],[1,0],[1,1]]
s10 = [[0,0],[-1,-1],[0,-1],[1,-1]]
s11 = [[0,0],[-1,1],[0,1],[1,1]]
s12 = [[0,0],[-1,-1],[-1,0],[-1,1]]
s13 = [[0,0],[0,1],[-1,1],[-2,1]]
s14 = [[0,0],[-1,0],[-1,1],[-1,2]]
s15 = [[0,0],[-1,0],[-1,-1],[-1,-2]]
s16 = [[0,0],[1,0],[1,1],[1,2]]
s17 = [[0,0],[0,1],[1,0],[1,1]]
s18 = [[0,0],[0,1],[1,1],[1,2]]
s19 = [[0,0],[0,-1],[1,-1],[1,-2]]
all_shape = [0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19]
result = []
for j in range(1,20):
    if j==1:
        ms1 = -1
        for x in range(N-2):
            for y in range(M-1):
                r = 0
                for i in range(4):
                    nx = x + s1[i][0]
                    ny = y + s1[i][1]
                    r += graph[nx][ny]
                if r > ms1:
                    ms1 = r
        result.append(ms1)
    elif j==2:
        ms2 = -1
        for x in range(N-2):
            for y in range(1,M):
                r = 0
                for i in range(4):
                    nx = x + s2[i][0]
                    ny = y + s2[i][1]
                    r += graph[nx][ny]
                if r > ms2:
                    ms2 = r
        result.append(ms2)
    elif j==3:
        ms3 = -1
        for x in range(N):
            for y in range(M-3):
                r = 0
                for i in range(4):
                    nx = x + s3[i][0]
                    ny = y + s3[i][1]
                    r += graph[nx][ny]
                if r > ms3:
                    ms3 = r
        result.append(ms3)
    elif j==4:
        ms4 = -1
        for x in range(N-3):
            for y in range(M):
                r = 0
                for i in range(4):
                    nx = x + s4[i][0]
                    ny = y + s4[i][1]
                    r += graph[nx][ny]
                if r > ms4:
                    ms4 = r
        result.append(ms4)
    elif j==5:
        ms5 = -1
        for x in range(N-2):
            for y in range(M-1):
                r = 0
                for i in range(4):
                    nx = x + s5[i][0]
                    ny = y + s5[i][1]
                    r += graph[nx][ny]
                if r > ms5:
                    ms5 = r
        result.append(ms5)
    elif j==6:
        ms6 = -1
        for x in range(N-1):
            for y in range(2,M):
                r = 0
                for i in range(4):
                    nx = x + s6[i][0]
                    ny = y + s6[i][1]
                    r += graph[nx][ny]
                if r > ms6:
                    ms6 = r
        result.append(ms6)
    elif j==7:
        ms7 = -1
        for x in range(N-2):
            for y in range(M-1):
                r = 0
                for i in range(4):
                    nx = x + s7[i][0]
                    ny = y + s7[i][1]
                    r += graph[nx][ny]
                if r > ms7:
                    ms7 = r
        result.append(ms7)
    elif j==8:
        ms8 = -1
        for x in range(N-2):
            for y in range(1,M):
                r = 0
                for i in range(4):
                    nx = x + s8[i][0]
                    ny = y + s8[i][1]
                    r += graph[nx][ny]
                if r > ms8:
                    ms8 = r
        result.append(ms8)
    elif j==9:
        ms9 = -1
        for x in range(N-1):
            for y in range(1,M-1):
                r = 0
                for i in range(4):
                    nx = x + s9[i][0]
                    ny = y + s9[i][1]
                    r += graph[nx][ny]
                if r > ms9:
                    ms9 = r
        result.append(ms9)
    elif j==10:
        ms10 = -1
        for x in range(1,N-1):
            for y in range(1,M):
                r = 0
                for i in range(4):
                    nx = x + s10[i][0]
                    ny = y + s10[i][1]
                    r += graph[nx][ny]
                if r > ms10:
                    ms10 = r
        result.append(ms10)
    elif j==11:
        ms11 = -1
        for x in range(1,N-1):
            for y in range(M-1):
                r = 0
                for i in range(4):
                    nx = x + s11[i][0]
                    ny = y + s11[i][1]
                    r += graph[nx][ny]
                if r > ms11:
                    ms11 = r
        result.append(ms11)
    elif j==12:
        ms12 = -1
        for x in range(1,N):
            for y in range(1,M-1):
                r = 0
                for i in range(4):
                    nx = x + s12[i][0]
                    ny = y + s12[i][1]
                    r += graph[nx][ny]
                if r > ms12:
                    ms12 = r
        result.append(ms12)
    elif j==13:
        ms13 = -1
        for x in range(2,N):
            for y in range(M-1):
                r = 0
                for i in range(4):
                    nx = x + s13[i][0]
                    ny = y + s13[i][1]
                    r += graph[nx][ny]
                if r > ms13:
                    ms13 = r
        result.append(ms13)
    elif j==14:
        ms14 = -1
        for x in range(1,N):
            for y in range(M-2):
                r = 0
                for i in range(4):
                    nx = x + s14[i][0]
                    ny = y + s14[i][1]
                    r += graph[nx][ny]
                if r > ms14:
                    ms14 = r
        result.append(ms14)
    elif j==15:
        ms15 = -1
        for x in range(1,N):
            for y in range(2,M):
                r = 0
                for i in range(4):
                    nx = x + s15[i][0]
                    ny = y + s15[i][1]
                    r += graph[nx][ny]
                if r > ms15:
                    ms15 = r
        result.append(ms15)
    elif j==16:
        ms16 = -1
        for x in range(N-1):
            for y in range(M-2):
                r = 0
                for i in range(4):
                    nx = x + s16[i][0]
                    ny = y + s16[i][1]
                    r += graph[nx][ny]
                if r > ms16:
                    ms16 = r
        result.append(ms16)
    elif j==17:
        ms17 = -1
        for x in range(N-1):
            for y in range(M-1):
                r = 0
                for i in range(4):
                    nx = x + s17[i][0]
                    ny = y + s17[i][1]
                    r += graph[nx][ny]
                if r > ms17:
                    ms17 = r
        result.append(ms17)
    elif j==18:
        ms18 = -1
        for x in range(N-1):
            for y in range(M-2):
                r = 0
                for i in range(4):
                    nx = x + s18[i][0]
                    ny = y + s18[i][1]
                    r += graph[nx][ny]
                if r > ms18:
                    ms18 = r
        result.append(ms18)
    elif j==19:
        ms19 = -1
        for x in range(N-1):
            for y in range(2,M):
                r = 0
                for i in range(4):
                    nx = x + s19[i][0]
                    ny = y + s19[i][1]
                    r += graph[nx][ny]
                if r > ms19:
                    ms19 = r
        result.append(ms19)
print(max(result))