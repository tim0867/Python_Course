# Note, when calling for an input using a string, and the answer is an integer then there will be an error
# This is because the answer it is looking for is basically a string, so 48 would look like "48" - an integer within string quotes
# To get around this, you must wrap the whole input function as an integer - 
# int(input("How old are you?\n"))  -  instead of  -  input("How old are you?\n")


age = int(input("How old are you?\n"))
decades = age/10
print(decades)


# The syntax below will error, as you can only concatenate strings not floats, so you have to change it back to a string

# age = int(input("How old are you?\n"))
# decades = age/10
# print("You are " + decades + " decades old!")


age = int(input("How old are you?\n"))
decades = age/10
print("You are " + str(decades) + " decades old!")

# To get the output as decades and years
# Python uses the operator // for whole number division - This will give the decades (or interger division)
# Python also has an operator for the remainder we use % - This will give the years (this remainder is also called modulus)

age = int(input("How old are you?\n"))

decades = age // 10
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old!")
