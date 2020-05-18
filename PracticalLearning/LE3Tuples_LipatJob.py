## Creating a Tuple

# Empty Tuple
my_tuple = ()
print(my_tuple) # Output: ()

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple) # Output: (1, 2, 3)

# Tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple) # Output: (1, "Hello", 3.4)

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Output: ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = 3, 4.6, "Dog"
print(my_tuple) # Output: (3, 4.6, "Dog")

# Tuple unpacking is also possible
a, b, c = my_tuple

print(a) # 3
print(b) # 4.6
print(c) # Dog


## Access Tuple Elements

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

print(my_tuple[0]) # 'p'
print(my_tuple[5]) # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# Nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Nested index
print(n_tuple[0][3]) # 's'
print(n_tuple[1][1]) # 4


## Negative Indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])


## Slicing

my_tuple = ('p', 'y', 't', 'h', 'o', 'n', '-', '2', 'L')

# Elements 2nd to 4th
# Output: ('y', 't', 'h')
print(my_tuple[1:4])

# Elements beginning to 2nd
# Output: ('p', 'y') 
print(my_tuple[:-7])

# Elements 8th to end
# Output: ('2', 'L')
print(my_tuple[7:])

# Elements beginning to end
# output: ('p', 'y', 't', 'h', 'o', 'n', '-', '2', 'L')
print(my_tuple[:])


## Changing a Tuple

my_tuple = (4, 2, 3, [6, 5])

# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9
print(my_tuple) # Output: (4, 2, 3, [9, 5])

# Tuples can be reassigned
my_tuple = ('p', 'y', 't', 'h', 'o', 'n', '-', '2', 'L')

# Output: ('p', 'y', 't', 'h', 'o', 'n', '-', '2', 'L')
print(my_tuple)

# Concatentation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('MCL', 'MCL', 'MCL')
print(("MCL", ) * 3)


## Deleting a Tuple

my_tuple = ('p', 'y', 't', 'h', 'o', 'n', '-', '2', 'L')

# Can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
# print(my_tuple)


## Tuple Methods

my_tuple = ('a', 'p', 'p', 'l', 'e')

print(my_tuple.count('p')) # Output: 2
print(my_tuple.index('l')) # Output: 3

