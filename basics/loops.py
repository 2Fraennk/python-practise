#!/usr/bin/env python3

# let's loop

# 1: simple while
count = 1
number = int(input("How many loops should we play? : "))

while count <= number:
    print("another loop : ", count)
    count += 1

# 2a . for with a list
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

# 2b . for with a dictionary
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key, value in ages.items():
    print(key, value)

# 3 loop with nested condition < consider right ingesting
counter2 = 1
while counter2 <= 25:
    if counter2 % 4 == 0:
        print(counter2)
    counter2 += 1

# 4a loop with continue
counter3 = 0
while counter3 < 10:
    if counter3 % 2 == 0:
        counter3 += 1
        continue
    print(f"odd number: {counter3}")
    counter3 += 1

# 4b loop with break
counter4 = 1
while counter4 < 10:
    if counter4 % 2 == 0:
        counter4 += 1
        break
    print(f"odd number with break: {counter4}")
    counter4 += 1
