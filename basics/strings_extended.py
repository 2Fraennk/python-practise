#!/usr/bin/env python3

# make a string lower case
upperCaseString = "THISISCRAZY"
upperCaseString2 = upperCaseString.lower()
print("This is a lower case string: " +  str(upperCaseString2))

# make a string upper case
lowerCaseString = "thisiscrazy"
upperCaseString3 = upperCaseString.upper()
print("This is an upper case string: " +  str(upperCaseString3))

# check a string for something
myString= "thisIsMyString"
myString2 = upperCaseString.isalpha()
print("myString is alphabetically :" + str(myString2))

# split a string
phrase = "This is a simple phrase"
words = phrase.split()
print(words)

# split an URL
url = "https://www.telekom.de/test.php"
print("url splitted: " + str(url.split('/')))
print("split before escape character: " + url.split('/')[0])
print("split after first match      : " + url.split('/')[1])
print("split after second match     : " + url.split('/')[2])
print("split after third match      : " + url.split('/')[3])

# put a comma into a existing string
lines = ['First line','Secound line','Third line']
print(lines)
linesWithNewLines = "\n".join(lines)
print(linesWithNewLines)

#
template = "Hello, my Name is {} from {}"
filledTemplate = template.format('Foo', 'Bar')
print(filledTemplate)

template2 = "Hello, my Name is {1} from {0}"
filledTemplate2 = template2.format('Foo', 'Bar')
print(filledTemplate2)