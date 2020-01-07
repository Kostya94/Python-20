
a = str(("file", "edit", "view", "navigate", "code", "refactor", "run", "tools", "window", "help"))
i = str(a.replace(",", ""))
dct = {}
for i in a:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
for i in sorted(dct):
    print(i, dct[i])