def main():
    T = int(input())
    for i in range(1,T+1):
        g = list(map(int,input().split()))
        print("#{} {}".format(i,round(sum(g)/len(g),1)))
    return

if __name__=="__main__":
    main()