#!/usr/bin/env python3

# typical way to transform a list
my_list = ['a', 'b', 'c', 'd']
print('initial list:' + str(my_list))

## create a new list and copy the transformed date into it
upper_case_list=[]
for character in my_list:
    upper_case_list.append(character.upper())

print('upper case list:' + str(upper_case_list))


# let's use list comprehension instead
my_list2 = ['a', 'b', 'c', 'd']
print('initial list2:' + str(my_list2))

upper_case_list2 = [character.upper() for character in my_list2]

print('upper case list2:' + str(upper_case_list2))

# it could be filtered as well
my_list3 = ['a', 'b', 'c', 'd']
print('initial list2:' + str(my_list3))

upper_case_list3 = [character.upper() for character in my_list3 if character in ['a', 'c']]

print('upper case list3:' + str(upper_case_list3))
