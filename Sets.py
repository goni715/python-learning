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
# fruits = {'banana', 'cherry', 'mango', 'apple'}
# for x in fruits:
#     print(x)
# output
# mango
# cherry
# banana
# apple


# Check if "banana" is present in the set:
# print("banana" in fruits)
# output = True


# Check if "banana" is NOT present in the set:
# print("banana" not in fruits)
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
# family = {'goni', 'ismail', 'marjan'}
# members = {'fatema', 'evan', 'mokbul'}
# family.update(members)
# print(family)
# output = {'evan', 'mokbul', 'fatema', 'marjan', 'goni', 'ismail'}




# Add any iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
#
# thisset.update(mylist)
# print(thisset)
# output = {'orange', 'kiwi', 'apple', 'cherry', 'banana'}




# Remove set Item
#
#
# using remove() method
# Note: If the item to remove does not exist, remove() will raise an error.
# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
# output = {'apple', 'cherry'}

# using discard() method
# Note: If the item to remove does not exist, discard() will NOT raise an error.
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("apple")
# print(fruits)
# output = {'banana', 'cherry'}


# using clear() method to empty the set
# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)
# output = set()



# Loop Sets
#
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)
# output =
# banana
# cherry
# apple






# Join sets
#
#
# join two sets using union() method
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)
# output = {1, 2, 3, 'b', 'c', 'a'}


# join two sets using | operator
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1 | set2
# print(set3)
# output = {1, 2, 3, 'c', 'b', 'a'}



# Join Multiple Sets using union() method
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# myset = set1.union(set2, set3, set4)
# print(myset)
# output = {1, 2, 'b', 3, 'John', 'cherry', 'a', 'Elena', 'bananas', 'apple', 'c'}



# Join Multiple Sets using | operator
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# myset = set1 | set2 | set3 |set4
# print(myset)
# output = {1, 2, 3, 'bananas', 'b', 'apple', 'John', 'cherry', 'a', 'Elena', 'c'}



# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
#
# x = {"a", "b", "c"}
# y = (1, 2, 3)
#
# z = x.union(y)
# print(z)
# output = {1, 2, 3, 'b', 'a', 'c'}
# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.




# Join sets using update() method
# The update() method inserts all items from one set into another.
#
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# output = {1, 2, 3, 'b', 'a', 'c'}


# Note: Both union() and update() will exclude any duplicate items.