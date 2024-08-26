# myset = {"apple", "banana", "cherry"}
# print(myset)
# print multiple times- Set items are unordered
# output = {'apple', 'banana', 'cherry'}
# output = {'banana', 'apple', 'cherry'}
# output = {'cherry', 'banana', 'apple'}



# set type checking
# print(type(myset))
# output = <class 'set'>



# Duplicates Not Allowed
# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(thisset)
# output = {'banana', 'apple', 'cherry'}





# Get the Length of a Set using len() function
# friends = {'Shakib', 'Abir', 'Habil', 'Somrat'}
# print(len(friends))
# output = 4




# Access Set items
#
#
# you can loop through the set items using a for loop
fruits = {'banana', 'cherry', 'mango', 'apple'}
# for x in fruits:
#     print(x)
# output
# mango
# cherry
# banana
# apple


# Check if "banana" is present in the set:
print("banana" in fruits)
# output = True


# Check if "banana" is NOT present in the set:
print("banana" not in fruits)
# output = False







# Add set items
#
#
# using add() method
# family = {'goni', 'ismail', 'marjan'}
# family.add('evan')
# print(family)
# output = {'ismail', 'goni', 'evan', 'marjan'}


# Add set
# To add items from another set into the current set, use the update() method.
#
family = {'goni', 'ismail', 'marjan'}
members = {'fatema', 'evan', 'mokbul'}
family.update(members)
print(family)
# output = {'evan', 'mokbul', 'fatema', 'marjan', 'goni', 'ismail'}




# Add any iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)
# output = {'orange', 'kiwi', 'apple', 'cherry', 'banana'}



