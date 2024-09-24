# biodata = {
#     "name" : "Osman Goni",
#     "age" : 23,
#     "university" : "BSMRSTU",
#     "location" : "Saidpur"
# }

# name = biodata['name']
# print(name)
# output = Osman Goni



# access dictionaries items
#
# using get() method
# name = biodata.get('name')
# print(name)
# output = Osman Goni


# keys() method
# The keys() method will return a list of all the keys in the dictionary.
#
# keysList = biodata.keys()  # output = dict_keys(['name', 'age', 'university', 'location'])
# print(list(keysList))
# output = ['name', 'age', 'university', 'location']


# values() method
# The values() method will return a list of all the values in the dictionary.
# list_of_values = biodata.values()
# print(list_of_values)
# output = dict_values(['Osman Goni', 23, 'BSMRSTU', 'Saidpur'])
# print(list(list_of_values))
# output = ['Osman Goni', 23, 'BSMRSTU', 'Saidpur']


# items() method
# The items() method will return each item in a dictionary, as tuples in a list.
#
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.items()
# print(x)
# output = dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])



# change dictionaries items
#
# thisdict ={
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["year"] = 2018
# print(thisdict['year'])
# output = 2018


# change item using update() method
#
# thisdict.update({"year": 2020})
# year = thisdict['year']
# print(year)
# output = 2020



# remove dictionaries item
# biodata = {
#     "name" : "Osman Goni",
#     "age" : 23,
#     "university" : "BSMRSTU",
#     "location" : "Saidpur"
# }



# using pop() method
#
# biodata.pop('age')
# print(biodata)
# output = {
#     'name': 'Osman Goni',
#     'university': 'BSMRSTU',
#     'location': 'Saidpur'
# }


# remove item using popitem() method
# popitem() method removes the item
#
# biodata = {
#     "name" : "Osman Goni",
#     "age" : 23,
#     "university" : "BSMRSTU",
#     "location" : "Saidpur"
# }
#
# biodata.popitem()
# print(biodata)
# output = {'name': 'Osman Goni', 'age': 23, 'university': 'BSMRSTU'}



# remove item using del keyword
# The del keyword removes the item with the specified key name:
#
#
# biodata = {
#     "name" : "Osman Goni",
#     "age" : 23,
#     "university" : "BSMRSTU",
#     "location" : "Saidpur"
# }
#
# del biodata['age']
# print(biodata)
# output = {'name': 'Osman Goni', 'university': 'BSMRSTU', 'location': 'Saidpur'}


# clear() method = clear the full dictionaries
#
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)
# output = { }



# loop in dictionaries
#
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# get only keys
# for x in thisdict:
#   print(x)
# output =
# brand
# model
# year



# Print all values in the dictionary, one by one:
# for x in thisdict:
#   print(thisdict[x])
# Ford
# Mustang
# 1964




# get only values
# You can also use the values() method to return values of a dictionary:
#
# for x in thisdict.values():
#   print(x)
# output =
# Ford
# Mustang
# 1964



# get only keys
# You can use the keys() method to return the keys of a dictionary:
#
# for x in thisdict.keys():
#   print(x)
# output =
# brand
# model
# year



# Loop through both keys and values, by using the items() method:
# for x, y in thisdict.items():
#   print(x, y)
# output =
# brand Ford
# model Mustang
# year 1964




# copy dictionaries
#
# using copy() method
#
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# mydict = thisdict.copy()
# print(mydict)
# output = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



# using dict() method
#
mydict = dict(thisdict)
print(mydict)
# output = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}