#zip=The zip() function combines multiple iterables (like lists, tuples, sets, strings) element-wise into tuples.
#It stops when the shortest iterable ends.
name=["ambati","praveen","seshu"]
score=[10,20,30]
zipped=zip(name,score)
print(list(zipped))
# o/p=[('ambati', 10), ('praveen', 20), ('seshu', 30)]

#with tuple
ids = (101, 102, 103)
grades = ("A", "B", "A")
print(list(zip(ids, grades)))
# Output: [(101, 'A'), (102, 'B'), (103, 'A')]

#with unequal length lists
l1 = [1, 2, 3]
l2 = ['a', 'b']
print(list(zip(l1, l2)))
# Output: [(1, 'a'), (2, 'b')]   (stops at shortest length)

#with strings
s1 = "abc"
s2 = "123"
print(list(zip(s1, s2)))
# Output: [('a', '1'), ('b', '2'), ('c', '3')]

#unzipped( reverse of zip)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)
print(nums)     # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')





