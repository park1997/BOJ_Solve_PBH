from itertools import permutation
grid = ["??b", "abc", "cc?"]
ques = []

for i in range(3):
    for j in range(3):
        if grid[i][j] == "?":
            ques.append([i,j])

permu = permutation(["a","b","b"],len(ques))
print(permu)
    


