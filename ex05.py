import sys
def main():
    N = int(sys.stdin.readline())
    for idx in range(N):
        g = list(map(int,sys.stdin.readline().split()))
        r = 0
        for i in g:
            if i%2==1:
                r += i
        print("#{} {}".format(idx,r))


if __name__=="__main__":
    main()