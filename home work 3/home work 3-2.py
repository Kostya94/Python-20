import itertools
numb = [2, 3, 4]
for L in range(2, len(numb)+1):
    print(list(itertools.combinations(numb, L)))
