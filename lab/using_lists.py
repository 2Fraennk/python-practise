#!/usr/bin/env python3

# init user list
users = []

# add users to user list
users.append('olaf')
users.append('mario')
users.append('bob')
users.append('guenther')

print('list: ' + str(users))

# remove bob from list
bobs_index = users.index('bob')
#users[bobs_index] = ''
del users[bobs_index]
rev_users = list(reversed(users))
print('new list without bob reversed: ' + str(rev_users))

# add melody to list
users.insert(0,'melody')
print('list: ' + str(users))

# slice users to return 3rd and 4th item
print('dedicated items from list: ' + str(users[2:4]))