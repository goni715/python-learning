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