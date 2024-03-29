# 10.26. Tuples and Mutability
'''
So far you have seen two types of sequential collections: strings, which are
made up of characters; and lists, which are made up of elements of any type.
One of the differences we noted is that the elements of a list can be modified,
but the characters in a string cannot.
    * In other words, strings are immutable and lists are mutable.

A tuple, like a list, is a sequence of items of any type. Unlike lists,
however, tuples are immutable. Syntactically, a tuple is a comma-separated
sequence of values. Although it is not necessary, it is conventional to
enclose tuples in parentheses:
    
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

Tuples are useful for representing what other languages often call records — some
related information that belongs together, like your student record. There is no
description of what each of these fields means, but we can guess. A tuple lets
us “chunk” together related information and use it as a single thing.

Tuples support the same sequence operations as strings and lists. For example,
the index operator selects an element from a tuple. A tuple can be the sequence
in a for-loop.

As with strings, if we try to use item assignment to modify one of the elements
of the tuple, we get an error.

julia[0] = 'X'
TypeError: 'tuple' object does not support item assignment

Of course, even if we can’t modify the elements of a tuple, we can make a
variable reference a new tuple holding different information. To construct
the new tuple, it is convenient that we can slice parts of the old tuple and
join up the bits to make the new tuple. So julia has a new recent film, and
we might want to change her tuple. We can easily slice off the parts we want
and concatenate them with the new tuple.
'''

print("\nExample 1:")
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

for field in julia:
    print(field)

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

'''
To create a tuple with a single element (but you’re probably not likely to do
that too often), we have to include the final comma, because without the final
comma, Python treats the (5) below as an integer in parentheses:
'''

print("\nExample 2:")
tup = (5,)
print(type(tup))

x = (5)
print(type(x))
