# 9.19 Character Classifications
'''
It is often helpful to examine a character and test whether it is upper- or lowercase, or whether it is a character or a digit. The string module provides several constants that are useful for these purposes. One of these, string.digits is equivalent to “0123456789”. It can be used to check if a character is a digit using the in operator.

The string string.ascii_lowercase contains all of the ascii letters that the system considers to be lowercase. Similarly, string.ascii_uppercase contains all of the uppercase letters. string.punctuation comprises all the characters considered to be punctuation. Run the following:


'''

import string


print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
