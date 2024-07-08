address = "Saidpur, Nilphamri"
print(address)

# inter type data
age = 23
print(type(age))


# floating type data// decimal type// দশমিক type data

weight = 52.6
print(type(weight))



# complex type data
x = 8699797j
print(type(x))



# boolean type data

booleanValue = True
print(type(booleanValue))


marjan_age = 7
evan_age = 2

print(marjan_age > evan_age)
# output = True


# binary type data
list1 = [1,2,3,4,5,6,230, 255]

bytesResult = bytes(list1)

print(bytesResult)

print(type(bytesResult))
#output=bytes


#binary bytearray type
list2 = [1,30,74,4,5,225,230, 255]

list2Result = bytearray(list2)

list2Result[1] = 100  #bytearray is mutable/changable

print(list2Result[1])
#output=100


#None type data
m=None
print(type(m))




#sequence type data


#1 list type data

li = ["Shakib", "Tamim", "Nasir", "Taskin", "Riyad"]
li[0]="Goni"

print(li)
#output = ['Goni', 'Tamim', 'Nasir', 'Taskin', 'Riyad']


#2 tuple type data

tup = ("Shakib", "Tamim", "Nasir", "Taskin", "Riyad") #tuple is immutable



#3 range type data

ran = range(6)
for i in ran:
    print(i)

    #output = 0 1 2 3 4 5
