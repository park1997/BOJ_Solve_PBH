import sys
from solution import init, destroy, update, updateByType, calculate

MAX_N = 100000

CMD_INIT = 100
CMD_DESTROY = 200
CMD_UPDATE = 300
CMD_UPDATE_TYPE = 400
CMD_CALC = 500

mType = [0 for _ in range(MAX_N)]
mTime = [0 for _ in range(MAX_N)]

def run():
    isOK = 0
    C = int(sys.stdin.readline())
    for c in range(C):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))
        if cmd == CMD_INIT:
            N = int(next(inputs))
            M = int(next(inputs))
            for i in range(N - 1):  mType[i] = int(next(inputs))
            for i in range(N - 1):  mTime[i] = int(next(inputs))
            init(N, M, mType, mTime)
            isOK = 1
        elif cmd == CMD_UPDATE:
            mID = int(next(inputs))
            mNewTime = int(next(inputs))
            update(mID, mNewTime)
        elif cmd == CMD_UPDATE_TYPE:
            mTypeID = int(next(inputs))
            mRatio256 = int(next(inputs))
            ret = updateByType(mTypeID, mRatio256)
            check = int(next(inputs))
            if ret != check:
                isOK = 0
        elif cmd == CMD_CALC:
            mA = int(next(inputs))
            mB = int(next(inputs))
            ret = calculate(mA, mB)
            check = int(next(inputs))
            if ret != check:
                isOK = 0
        else:
            isOK = 0
    destroy()
    return isOK


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
