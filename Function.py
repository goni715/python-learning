print("This is Function File");

# def = define
def my_function():
  print("Hello from a function")

my_function()



def my_function2(fname):
  print(fname + " Goni")

my_function2("Osman")


# parameters vs arguments
# parameters are the named variables
# here, parameters = fname

# arguments are the actual values passed to the function when it is called.
# here, arguments = "Osman"



#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# I will receive tuple as params for arbitrary function.
#
def my_function3(*kids):
  # print(kids)  ('Evan', 'Marjan', 'Bishwas')== this is tuple
  print("The youngest child is " + kids[0]) #output = The youngest child is Evan

my_function3("Evan", "Marjan", "Bishwas")



# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
#
def keywordFunction(child1, child3, child2):
    print("The youngest child is "+ child3)
keywordFunction(child1= "Marjan Hossain", child2= "Abdur Rahman Bishwas", child3= "Evan Ahmed")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def arbitraryKeyword(**kid):
# print(kid) //output = {'fname': 'Evan', 'lname': 'Ahmed'} == this is dictionary
  print("His last name is " + kid["lname"])

arbitraryKeyword(fname = "Evan", lname = "Ahmed")