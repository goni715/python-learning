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
# 
print("A") if a > b else print("B")


