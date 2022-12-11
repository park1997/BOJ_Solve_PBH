import sys
from solution import init, addRestaurant, removeRestaurant, order, beFriend, recommend

CMD_INIT = 100
CMD_ADD_RESTAURANT = 200
CMD_REMOVE_RESTAURANT = 300
CMD_ORDER = 400
CMD_BE_FRIEND = 500
CMD_RECOMMEND = 600


def run():
    query = int(input())
    ok = False
    n = 0
    for i in range(query):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            n = int(next(input_iter))
            list_px = list(map(int, input().split()))
            list_py = list(map(int, input().split()))
            init(n, list_px, list_py)
            ok = True
        elif cmd == CMD_ADD_RESTAURANT:
            pID = int(next(input_iter))
            x = int(next(input_iter))
            y = int(next(input_iter))
            addRestaurant(pID, x, y)
        elif cmd == CMD_REMOVE_RESTAURANT:
            pID = int(next(input_iter))
            removeRestaurant(pID)
        elif cmd == CMD_ORDER:
            uID = int(next(input_iter))
            pID = int(next(input_iter))
            order(uID, pID)
        elif cmd == CMD_BE_FRIEND:
            uID1 = int(next(input_iter))
            uID2 = int(next(input_iter))
            beFriend(uID1, uID2)
        elif cmd == CMD_RECOMMEND:
            uID = int(next(input_iter))
            ret = recommend(uID)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
    return ok

if __name__ == '__main__':
	# sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)
