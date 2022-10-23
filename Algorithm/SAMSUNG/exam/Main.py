import sys

from solution import init, add, cost

CMD_INIT = 1
CMD_ADD = 2
CMD_COST = 3

def run():
	q = int(input())
	okay = False
	sCityArr = []
	eCityArr = []
	mCostArr = []

	for i in range(q):
		inputarray = input().split()
		cmd = int(inputarray[0])

		if cmd == CMD_INIT:
			okay = True
			n = int(inputarray[1])
			for j in range(n):
				edgeinput = input().split()
				sCityArr.append(int(edgeinput[0]))
				eCityArr.append(int(edgeinput[1]))
				mCostArr.append(int(edgeinput[2]))
			ans = int(input())
			ret = init(n, sCityArr, eCityArr, mCostArr)
			if ans != ret:
				okay = False
		elif cmd == CMD_ADD:
			sCity = int(inputarray[1])
			eCity = int(inputarray[2])
			mCost = int(inputarray[3])
			add(sCity, eCity, mCost)
		elif cmd == CMD_COST:
			mHub = int(inputarray[1])
			ans = int(inputarray[2])
			ret = cost(mHub)
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, 2):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)
        
