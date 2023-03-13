from collections import defaultdict

def init(N:int, M:int, mType:list , mTime:list) -> None:
    global NN, mType_, mTime_, q, prefix_sum
    NN = N
    mType_ = mType[:]
    mTime_ = mTime[:]
    q = defaultdict(int)
    prefix_sum = [0 for _ in range(N)]
    for i in range(N - 1):
        prefix_sum[i + 1] = prefix_sum[i] + mTime[i]

def destroy() -> None:
    mType_.clear()
    mTime_.clear()

def update(mID:int, mNewTime:int) -> None:
    q[mID + 1] += (mNewTime - mTime_[mID])
    mTime_[mID] = mNewTime

def updateByType(mTypeID:int, mRatio256:int) -> int:
    total = 0
    for i in range(NN - 1):
        if mTypeID == mType_[i]:
            update = update_val(mTime_[i], mRatio256)
            total += update
            mTime_[i] = update
        prefix_sum[i + 1] = prefix_sum[i] + mTime_[i]
    q.clear()
    return total

def calculate(mA:int , mB:int) -> int:
    if mA > mB:
        mA, mB = mB, mA
    output = prefix_sum[mB] - prefix_sum[mA]
    for id_ in q:
        if mA < id_ <= mB:
            output += q[id_]
    return output

def update_val(orig:int, ratio:int) -> int:
    return (orig * ratio) // 256
