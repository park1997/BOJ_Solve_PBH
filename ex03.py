a = [[2, 2, 5, 6, 9], [5, 4, 1, 6, 6], [4, 2, 3, 5, 7]]
a.sort(key=lambda x: (-x[4], -x[0], -x[1]))
print(a)


b = [[2, 2, 5, 6, 9], [5, 4, 1, 6, 6], [4, 2, 3, 5, 7]]
b = list(sorted(b , key = lambda x : (-x[4],-x[0],-x[1])))
print(b)

