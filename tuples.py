#!/usr/bin/env python3

# let's try tuples

# create an immutable tuple
tuple1 = (1, 2, 3, 4)
print('tuple1: ' + str(tuple1))

# extend a new tuple with an existing one
tuple2 = tuple1 + (5,)
print('tuple2: ' + str(tuple2))

# serialize a tuple's values into dedicated variables
a,b,c,d = tuple1
print('a: ' + str(a))
print('b: ' + str(b))
print('c: ' + str(c))
print('d: ' + str(d))

# serialize a tuple's values into output
a,b,c,d = tuple1
print('The numbers are: %a, %a, %a, %a' % (tuple1))