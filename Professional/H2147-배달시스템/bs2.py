from typing import List
UserTotal = {}
House = {}
Friends = {}
Restaurant = {}
Num = 0
 
def init(N:int, px:List[int], py:List[int]) -> None:
    global House, Friends, Restaurant, Num
    House.clear()
    Friends.clear()
    Restaurant.clear()
    Num = N
    for n in range(N):
        UserTotal[n] = dict()
        House[n] = (px[n], py[n])
        Friends[n] = set()
    return
 
def addRestaurant(pID:int, x:int, y:int) -> None:
    Restaurant[pID] = [0]*Num
    for n in UserTotal:
        UserTotal[n][pID] = - (abs(House[n][0]-x) + abs(House[n][1]-y)) * 1e6 - pID
    return
 
def removeRestaurant(pID:int) -> None:
    del Restaurant[pID]
    for n in UserTotal:
        del UserTotal[n][pID]
    return
 
def order(uID:int, pID:int) -> None:
    UserTotal[uID][pID] += 1e13
    Restaurant[pID][uID] += 1e13
 
    for friend in Friends[uID]:
        UserTotal[friend][pID] += 1e13
    return
 
def beFriend(uID1:int, uID2:int) -> None:
    Friends[uID1].add(uID2)
    Friends[uID2].add(uID1)
    for rest in Restaurant:
        UserTotal[uID1][rest] += Restaurant[rest][uID2]
        UserTotal[uID2][rest] += Restaurant[rest][uID1]
    return
 
def recommend(uID:int) -> int:
    # tmp = sorted(UserTotal[uID].values())
    tmp = list(UserTotal[uID].values())
    for _ in range(9):
        tmp.pop(tmp.index(max(tmp)))
    return 1e6 - max(tmp)%1e6