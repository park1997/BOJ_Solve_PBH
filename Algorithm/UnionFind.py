def getParent(parent, x):
    # 재귀함수의 종료부분
    if parent[x] == x:
        return x
    