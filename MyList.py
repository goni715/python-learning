list1 = [1, 2, 3, 4, 5, 6]

#change list item
list1[1] = 10

# print(list1)
#output = [1, 10, 3, 4, 5, 6]


list2 = ["Shakib", "Tamim", "Taskin", "Nasir"]

list3 = [True, False, True, False]


#list length
#
thislist = ["apple", "banana", "cherry"]
# print(len(thislist))



# Add list item
#
#using append() method
thislist.append('orange')
# print(thislist)
#output = ['apple', 'banana', 'cherry', 'orange']


#using insert() method
thislist2 = ["apple", "banana", "cherry"]
thislist2.insert(1, 'orange')
# print(thislist2)
#output = ['apple', 'orange', 'banana', 'cherry']



#extend list
#
thislist3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical)
# print(thislist3)
#output = ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']



#extend list -- Add Any Iterable
#
thislist4 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist4.extend(thistuple)
# print(thislist4)
# output = ['apple', 'banana', 'cherry', 'kiwi', 'orange']





# remove list item

# remove specific item using remove() method
#
players = ['Shakib', 'Tamim', 'Nasir', 'Taskin']
# players.remove("Taskin")
# print(players)
# output = ['Shakib', 'Tamim', 'Nasir']



# remove specific index
#
# players.pop(0)
# print(players)
# output = ['Tamim', 'Nasir', 'Taskin']



# If you do not specify the index, the pop() method removes the last item.
#
# players.pop()
# print(players)
# output = ['Shakib', 'Tamim', 'Nasir']


# The del keyword also removes the specified index:
#Remove the first item:
#
fruits = ["apple", "banana", "cherry"]
# del fruits[0]
# print(fruits)
# output = ['banana', 'cherry']




# The del keyword can also delete the list completely.
#
# del fruits
# print(fruits) error show



# The clear() method empties the list.
# The list still remains, but it has no content.
# fruits.clear()
# print(fruits)
# output = []




# for loop
# You can loop through the list items by using a for loop:
#
actors = ['Shakib', "Salman", 'Riaz', 'Siam', 'Raj']

# for x in actors:
#   print(x)

# output =
# Shakib
# Salman
# Riaz
# Siam
# Raj




# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.

# for i in range(len(actors)):
#    print(actors[i])

# output =
# Shakib
# Salman
# Riaz
# Siam
# Raj




# while loop
# You can loop through the list items by using a while loop.
#
i = 0
while i < len(actors):
    # print(actors[i])
    i = i + 1

# output =
# Shakib
# Salman
# Riaz
# Siam
# Raj







# list comprehension
#
# syntax
# output_list = []
# for element in list:
#     output_list.append(output_expression)


# example-01
#
# numbers = [1, 2, 3, 4, 5]
#
# squares = []
# for number in numbers:
#     squares.append(number**2)
#
# print(squares)
# output = [1, 4, 9, 16, 25]



# list comprehesion syntax:
# [output_expression for element in list]
#
# Example 02
#
# numbers = [1, 2, 3, 4, 5]
# squares = [number**2 for number in numbers]
#
# print(squares)
# output = [1, 4, 9, 16, 25]






# sort list using sort() method
#
# Sort List Alphanumerically
# fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruits.sort()
# print(fruits)
# output = ['banana', 'kiwi', 'mango', 'orange', 'pineapple']



# Sort the list numerically:
#
# numbers = [100, 50, 65, 82, 23]
# numbers.sort()
# print(numbers)
# output = [23, 50, 65, 82, 100]




# Sort Descending
# To sort descending, use the keyword argument reverse = True
#
# fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruits.sort(reverse = True)
# print(fruits)
# output = ['pineapple', 'orange', 'mango', 'kiwi', 'banana']



# Sort the number list descending:
# numbers = [100, 50, 65, 82, 23]
# numbers.sort(reverse = True)
# print(numbers)
# output = [100, 82, 65, 50, 23]




# Python copy a list
#
# copy a list using copy() method
# fruits = ["apple", "banana", "cherry"]
# fruits2 = fruits.copy()
# print(fruits2)
# output = ['apple', 'banana', 'cherry']



# copy a list using list() method
# fruits = ["apple", "banana", "cherry"]
# fruits2 = list(fruits)
# print(fruits2)
# output = ['apple', 'banana', 'cherry']


# copy a list using slice (:) operator
# fruits = ["apple", "banana", "cherry"]
# fruits2 = fruits[:]
# print(fruits2)
# output = ['apple', 'banana', 'cherry']






# Python - Join Lists
#
#
# join two list using plus (+) operator
#
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# list3 = list1 + list2
# print(list3)
# output = ['a', 'b', 'c', 1, 2, 3]



# join two list by appending all items of another list
#
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3, 4]
#
# for x in list2:
#   list1.append(x)
#
# print(list1)
# output = ['a', 'b', 'c', 1, 2, 3, 4]




# join two list using extend() method
#
list1 = ["a", "b", "c", "goni"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# output = ['a', 'b', 'c', 'goni', 1, 2, 3]


