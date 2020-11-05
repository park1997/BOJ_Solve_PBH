#잃어버린 괄호
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e[0]-sum(e[1:]))
