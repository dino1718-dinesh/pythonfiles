#strings are immutable
name="mango"
sentence="""
hello my name is dinesh
what about you"""

#printing all characters in the any string
for character in sentence:
    print(character)

#printing the character at particular index
print( "the particalar character is :",name[3])



# finding the length of the string
print("length of the string :",len(name))

#positive slicing 
print("slicing :",name[0:4])
print("slicing :",name[2:5])
print("slicing :",name[0:])

#negative slicing
print("slicing :",name[0:-3]) # in this we have to slice like length of string -negative number we get [0:2]
print("slicing :",name[-1:-3])# in this case we have [4:2] it is not possible
# print("slicing :",name[0:4])
# print("slicing :",name[0:4])


