mytuple = ("apple", "banana", "cherry")

# tuples are unchangable or immutable
# mytuple[1] = "Mango" #error show
#print(mytuple)



# Tuples Allow Duplicates
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")



# Access Tuples
#
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])
# output = banana




# Negative Indexing
# Negative indexing means start from the end.
#
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])
# output = cherry


# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
#
#
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])
# output = ('cherry', 'orange', 'kiwi')
#
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included






# Update Tuples
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#
# add items
# FriendsTuple = ("Shakib", "Abir", "Kommon", "Habil")
# FriendsList = list(FriendsTuple)
# print(FriendsList)
# output= ['Shakib', 'Abir', 'Kommon', 'Habil']
#
# FriendsList.append('Shishir')
# print(FriendsList)
# output= ['Shakib', 'Abir', 'Kommon', 'Habil', 'Shishir']
#
# FriendsTuple = tuple(FriendsList)
#
# print(FriendsTuple)
# output = ('Shakib', 'Abir', 'Kommon', 'Habil', 'Shishir')



# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
# y = ("orange",)


# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
#
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)
# ('apple', 'banana', 'cherry', 'orange')



# Remove Items
# fruitsTuple = ("apple", "banana", "cherry")
# y = list(fruitsTuple)
# y.remove("apple")
# fruitsTuple = tuple(y)
# print(fruitsTuple)
# output = ('banana', 'cherry')




# Unpack Tuples
#
# fruits = ("apple", "banana", "cherry")
# (first, second, third) = fruits
# print(first)
# output = apple

# print(second)
# output = banana

# print(third)
# output = cherry



# friends = ("Shakib", "Abir", "Habil", "Shishir")
# (a, b, c, d, ) = friends
# print(c)
# output = Habil



# unpack tuple using Asterisk *
# fruitsTuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (first, *rest) = fruitsTuple
# print(rest)
# output = ['banana', 'cherry', 'strawberry', 'raspberry']

# (first, *rest, last) = fruitsTuple
# print(first)
# output = apple

# print(rest)
# output = ['banana', 'cherry', 'strawberry']

# print(last)
# output = raspberry










# Loop tuple
#
#
# using for loop
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
# output=
# apple
# banana
# cherry


# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
#
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# output=
# apple
# banana
# cherry





# join two tuples
#
# using + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# output = ('a', 'b', 'c', 1, 2, 3)



# multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# output = ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

