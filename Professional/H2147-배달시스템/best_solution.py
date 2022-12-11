from typing import List
from collections import defaultdict
 
def init(N:int, px:List[int], py:List[int]) -> None:
    global restaurant, user_home, value, friendlist, restuarant_order_log
    user_home = defaultdict(list)
    for i in range(N):
        user_home[i] = [px[i], py[i]]
    restaurant = defaultdict(list)
    restuarant_order_log = defaultdict(lambda: defaultdict(int))
    value = defaultdict(lambda: defaultdict(int))
    friendlist = defaultdict(list)
             
 
def addRestaurant(pID:int, x:int, y:int) -> None:
    restaurant[pID] = [x, y]
    for uID, user_xy in user_home.items():
        value[uID][pID] = - (abs(user_xy[0] - x) + abs(user_xy[1] - y))*(10**6) - pID
         
 
def removeRestaurant(pID:int) -> None:
    del restaurant[pID]
    for uID in user_home:
        del value[uID][pID]
 
def order(uID:int, pID:int) -> None:
    value[uID][pID] = value[uID][pID] + (10**13)
    restuarant_order_log[uID][pID] = restuarant_order_log[uID][pID] + (10**13)  
 
    for uID_friend in friendlist[uID]:
        value[uID_friend][pID] = value[uID_friend][pID] + (10**13)
         
     
def beFriend(uID1:int, uID2:int) -> None:
    friendlist[uID1].append(uID2)
    friendlist[uID2].append(uID1)
    for tmp in restaurant:
        value[uID1][tmp] = value[uID1][tmp] + restuarant_order_log[uID2][tmp]
        value[uID2][tmp] = value[uID2][tmp] +restuarant_order_log[uID1][tmp]
    # return
 
def recommend(uID:int) -> int:
    tmp_value = list(value[uID].values())
 
    for _ in range(9):
        tmp_value.pop(tmp_value.index(max(tmp_value)))
     
    top_ten = max(tmp_value)%(10**6)
    top_ten = 10**6 - top_ten 
 
    return top_ten