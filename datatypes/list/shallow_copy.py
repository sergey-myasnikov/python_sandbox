"""
    A shallow copy duplicates an object's top-level properties
while keeping references to any nested objects or mutable data.
"""


from copy import copy, deepcopy


# Question from Tech Interview in KL October 14th 2026
a = [0, [0]]
b = a
b[0] = 1
c = a[:]
d = copy(a)
e = deepcopy(a)
d[1][0] = 1

print(a, b, c, d, e)


"""
------------------------------------------------------------
"""

a = [1, 2, [3]]

a_copy_1 = a[:]
a_copy_2 = a.copy()
a_copy_3 = copy(a)  # Same as a.copy() with an overhead to call module function

print(a is a_copy_1)
print(a is a_copy_2)
print(a is a_copy_3)

print(a[0] is a_copy_1[0])
print(a[0] is a_copy_2[0])
print(a[0] is a_copy_3[0])

print(a[2] is a_copy_1[2])
print(a[2] is a_copy_2[2])
print(a[2] is a_copy_3[2])