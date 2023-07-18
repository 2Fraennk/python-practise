#!/usr/bin/env python3
from typing import Any

# Create the split_names Function to Separate Names
name = "Alexander van Example"


def split_names(name):
    splited = name.split(" ")
    firstname = splited[0]
    lastname = splited[1::1]
    lastnameAsString = " ".join(lastname)
    return {
        "firstname": firstname,
        "lastname": lastnameAsString,
    }


result = split_names(name)
print("firstname : ", result['firstname'])
print("lastname : ", result['lastname'])

assert result == {
    'firstname': 'Alexander',
    'lastname': 'van Example',
}, f"name should be : Alexander van Example"


# Create the is_palindrome Function to Determine if a String or Number Is a Palindrome
name2 = "anna"
def reverse(name2):
    reverseString = name2[::-1]
    return reverseString == name2
print(name,", the name is right.")


assert reverse(name2) == True, f"Warning: {name2} is not ap palindrome"
print(name2,"is a palindrom.")
