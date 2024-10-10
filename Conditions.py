# Python Conditions and If statements
#
# Following conditions can be used in several ways, most commonly in "if statements" and loops.
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b



# Example-01
marjan_age = 8
evan_age = 1

if marjan_age > evan_age:
    print('Marjan is elder than Evan')
elif marjan_age == evan_age:   # elif = else if
    print('Age of Marjan & Evan is same')
else:
    print('Marjan is younger than Evan')




# Short Hand If
# Example
# One line if statement:
a = 20
b = 10
if a > b: print("a is greater than b")



# Short Hand If ... Else
# One line if else statement:
# This technique is known as Ternary Operators
#
print("A") if a > b else print("B")
# output = A



# One line if else statement, with 3 conditions:
x = 330
y = 330

print("A") if x > y else print("Equal") if x == y else print("B")
# output: Equal





# using logical operator = and or not
#
# and operator
p = 200
q = 33
r = 500
if p > q and r > p:
  print("Both conditions are True")


# or operator
if p > q or p > r:
  print("At least one of the conditions is True")


# using not operator
m = 33
n = 200
if not m > n:
  print("m is NOT greater than n")



# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
#
if n > m:
  pass