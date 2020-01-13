import collections
a = ("file", "edit", "view", "navigate", "code", "refactor", "run", "tools", "window", "help")
data_str = ''.join(a)

c = collections.Counter(data_str).most_common(1)
print(c)
