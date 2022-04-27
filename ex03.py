def main():
    T = int(input())
    for t in range(1,T+1):
        num = int(input())
        case = [0]*101
        for c in list(map(int,input().split())):
            case[c] += 1
        case = list(reversed(case))
        print("#{} {}".format(num,100 - case.index(max(case))))
if __name__=="__main__":
    main()