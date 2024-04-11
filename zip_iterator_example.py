# if you wish to run over multiple list items, you can do it with easy zip structure.

foo = [1, 2, 3]
bar = [4, 5, 6]

for item_foo, item_bar in zip(foo, bar):
    print(item_foo, item_bar)

# you can stack multiple lists

zee = [7, 6, 9]

for item_foo, item_bar, item_zee in zip(foo, bar, zee):
    print(item_foo, item_bar, item_zee)

# another cool and useful tip is to do it with two dicts

d = {'a': 5, 'b': 6, 'c': 3}
d2 = {'a': 6, 'b': 7, 'c': 3}

for (k, v), (k2, v2) in zip(d.items(), d2.items()):
    print(k, v)
    print(k2, v2)
