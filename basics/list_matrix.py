#!/usr/bin/env python3

# let's try lists

# list as matrix with integers
my_matrix = [[1, 2, 3],
             [4, 5, 6]]
print(my_matrix)

# row count
print('amount of rows: ' + str(len(my_matrix)))

# column count
# count exemplary the objects of the first row
print('amound of columns: ' + str(len(my_matrix[0])))

# print dedicated row , column
print('value of row+column is: ' + str(my_matrix[1][2]))