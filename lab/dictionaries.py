#!/usr/bin/env python3

# create email dictionary and add initial items
email = {}
assert email == {}

email = dict(craig='craig@example.org', henry='henry@example.org', pamela='pam@example.org')
print(email)
assert email == {
    'craig': 'craig@example.org',
    'henry': 'henry@example.org',
    'pamela': 'pam@example.org',
}, f"Expected `emails` to be {{ 'craig':'craig@example.org', 'henry':'henry@example.org', 'pamela':'pam@example.org'}}"

# remove craig and add dalton
del email['craig']
print('Is craig still there? ' + str(email) in 'craig')
assert str(email) not in 'craig'

email['dalton'] = 'dalton@example.org'
print(email)
print('Is dalton already there? ' + str(email) in 'dalton')
#assert str(email) in 'dalton'

# return a list of keys and values from the dictionary
keys = email.keys()
users = list(keys)
print('here are the users: ' + str(users))
assert users[0] in 'henry'

values = email.values()
addresses = list(values)
print('here are the values: ' + str(addresses))
assert addresses == [
    'henry@example.org',
    'pam@example.org',
    'dalton@example.org'
]

# return a list of tuples called pairs representing the key/value pairs in emails
items = email.items()
pairs = list(items)
print('here are the items as tuples: ' + str(pairs))
assert pairs == [
    ('henry', 'henry@example.org'),
    ('pamela', 'pam@example.org'),
    ('dalton', 'dalton@example.org')
]
