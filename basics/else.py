#!/usr/bin/env python3

# let's loop

# 1: simple (almost useless) case
count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("While loop completed")

# 2: for-else : it makes sense when use conditional break out
colors = ['green', 'red', 'blue', 'orange', 'yellow']
colors2 = []
for color in colors:
    if color == 'orange':
        print('Orange found')
        break
else:
    print('nothing found')

# 3: range
my_range = range(10)
my_list = list(my_range)

print(my_list)
