a = [1, 2, 3, 3, 2, 2, 4]
dct = {}
for i in a:
    if i in dct:
            dct[i] += 1
    else:
        dct[i] = 1
for i in sorted(dct):
    print(i, dct[i])