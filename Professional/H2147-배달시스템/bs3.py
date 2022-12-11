	
from collections import defaultdict
 
N_TOP = 10
def init(N, px, py):
    global users, pUser, pRest, rOrder, rTotal, rDist, friends
    users = [u for u in range(N)]
    pUser = [(px[u], py[u]) for u in users]
    pRest = defaultdict(tuple)
 
    rOrder = [defaultdict(int) for u in users]
    rTotal = [defaultdict(int) for u in users]
    rDist = [{} for u in users]
    friends = [[] for u in users]
 
def addRestaurant(pID, x, y):
    pRest[pID] = (x, y)
    for u in users:
        rDist[u][pID] = abs(pUser[u][0] - pRest[pID][0]) + abs(pUser[u][1] - pRest[pID][1])
 
def removeRestaurant(pID):
    del pRest[pID]
    for u in users:
        del rDist[u][pID]
        if pID in rOrder[u].keys():
            del rOrder[u][pID]
        if pID in rTotal[u].keys():
            del rTotal[u][pID]
 
def order(uID, pID):
    rOrder[uID][pID] += 1
    for u in [uID] + friends[uID]:
        rTotal[u][pID] += 1
 
def beFriend(uID, uID2):
    friends[uID].append(uID2)
    friends[uID2].append(uID)
    for r in rOrder[uID2].keys():
        rTotal[uID][r] += rOrder[uID2][r]
    for r in rOrder[uID].keys():
        rTotal[uID2][r] += rOrder[uID][r]
 
def recommend(uID):
    ranking = defaultdict(list)
    for pID, score in rTotal[uID].items():
        ranking[score].append(pID)
 
    topten = []
    for score in sorted(ranking.keys(), reverse=True):
        if len(topten) + len(ranking[score]) < N_TOP-1:
            topten += ranking[score]
        else:
            for pID in sorted(ranking[score], key=lambda x: (rDist[uID][x], x)):
                topten += [pID]
                if len(topten) == N_TOP:
                    return pID
 
    for pID, dist in sorted(rDist[uID].items(), key=lambda x: (x[1], x[0])):
        if pID not in topten:
            topten += [pID]
            if len(topten) == N_TOP:
                return pID
    return -1