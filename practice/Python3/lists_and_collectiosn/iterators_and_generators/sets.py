# sets comparision
first = {1, 2}
second = {1, 2}
third = {1, 2, 3}

is_equal = first.issubset(second) and second.issubset(first)
print(is_equal)
is_equal = first == second
print(is_equal)

# sort
print(sorted(third))

# search
print(1 in third)
print(third.issuperset(first))

# add and remove
third.add(4)
third.add(5)
third.add(6)
third.add(4)

print(third)
third.remove(4)
print(third)
print(third.pop())
print(third)
# third.clear()
print(third)

# iterating over a set
for c in third:
    print(c)


first = {1, 2, 3}
second = {3, 4, 5}

print(first.union(second))
print(first.difference(second))
print(second.difference(first))
print(first.intersection(second))
print(first.symmetric_difference(second))
