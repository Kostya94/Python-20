
import collections
a = [2, 3, 4, 1, 2, 3, 2, 2]
'''dct = {}
for i in a:
    if i in dct:
            dct[i] += 1
    else:
        dct[i] = 1
for i in sorted(dct):
    print(i, dct[i])'''
'''a_set = set(a)
most_common = None
qty_most_common = 0
for item in a_set:
    qty = a.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item
print(most_common)'''

c = collections.Counter(a).most_common(1)
print(c)