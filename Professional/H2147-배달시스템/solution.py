from typing import List
import heapq
from collections import defaultdict

def init(N:int, px:List[int], py:List[int]) -> None:
    global n, rUser, rRest, rOrder, tOrder, rFriend, pq
    n = N
    rUser = [[] for _ in range(N)] # rUser[uID] = (x,y)
    rRest = defaultdict(list) # rRest[pID] = (x,y)
    rOrder = [defaultdict(int) for _ in range(N)]  # rOrder[uID][pID] = cnt 개인주문
    tOrder = [defaultdict(int) for _ in range(N)]  # tOrder[uID][pID] = cnt 토탈주문(개인+친구)
    rFriend = [[] for _ in range(N)] # rFriend[uID] = (uID1,uID2,,,,) 친구정보
    pq = defaultdict(list) # pq[uID] = (hash(cnt,dist,pID)),,,,, 우선순위 탐색

    for i in range(N):
        rUser[i] = (px[i], py[i])


def addRestaurant(pID:int, x:int, y:int) -> None:
    

    return


def removeRestaurant(pID:int) -> None:


    return 

def order(uID:int, pID:int) -> None:
    return

def beFriend(uID1:int, uID2:int) -> None:
    return

def recommend(uID:int) -> int:
    return 0