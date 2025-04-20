print("This is Function File");

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

def my_function3(*kids):
  # print(kids)  ('Evan', 'Marjan', 'Bishwas')== this is tuple
  print("The youngest child is " + kids[0]) #output = The youngest child is Evan

my_function3("Evan", "Marjan", "Bishwas")

