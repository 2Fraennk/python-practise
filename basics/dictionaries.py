#!/usr/bin/env python3

# let's try dictionaries

# create dictionary and call the value from a dedicated key
ages = {'tom': 34, 'henry': 62, 'jim': 25}
print('age of tom: ' + str(ages['tom']))

# add key and value to a dictionary
ages['amanda'] = 22
print('whole ages dictionary with new key-value : ' + str(ages))

# change values of existing keys inside a dictionary
ages['tom'] = 33
print('new age of tom: ' + str(ages['tom']))

# remove values of existing keys inside a dictionary
del ages['henry']
print('ages without henry: ' + str(ages))

# in functions using dictionary
print('henry is there: ' + str('henry' in ages))
print('tom is there: ' + str('tom' in ages))

# alternate way to create dictionary
lastnames = dict(tom='hanks', amanda='smith', jim='kirk')
print('lastname of tom: ' + str(lastnames['tom']))

# functions: get keys of a dictionary
keys_lastnames = lastnames.keys()
print('keys_lastnames: ' + str(list(keys_lastnames)))

# functions: get values of all keys from dictionary
values_lastnames = lastnames.values()
print('values_lastnames: ' + str(list(values_lastnames)))

# functions: get all items keys+values from dictionary
items_lastnames = lastnames.items()
print('items_lastnames: ' + str(list(items_lastnames)))