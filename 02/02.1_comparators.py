# The 6 comparators
# <   -  less than
# <=  -  less than equal to
# ==  -  equal
# >=  -  greater than equal to
# >   -  greater than
# !=  -  not equal

temp = 95   # This is assigning the value of 95 to the variable of temp
temp == 95  # This is a comparision, like asking the question "Is the temp equal to 95?" When run it will reply either 'True' or 'False'

# An elif statement is 'else' and 'if' together

temp = 50
if temp > 80:
    print("It's far too hot")
    print("Stay indoors and have a cold drink")
elif temp < 60:
    print("Brrrrr, It's too cold!")
    print("Stay indoors today, and put the fire on!")
else:
    print("Have a great day outside")



# To shorten the code, you can combine statements with 'or' as long as you are using the same print statement

temp = 70
if temp > 80 or temp < 60:
    print("Stay indoors")
else:
    print("Have a great day outside")


# You can combine 2 ouput statements using 'and' - Remember that both statements need to be true for the output to be true

temp = 60
weather = "rain"
if temp < 80 and weather != "rain":
    print("Enjoy the outdoors")
else:
    print("Stay indoors, don't go out today")
    


# As a little test, I combined 'if, or, and' statements -- Pretty cool

temp = 60
weather = "sun"
if temp > 80 or temp < 50 and weather != "rain":
    print("Don't go out today")
else:
    print("Go outdoors")



# Step it up a gear and introduce Boolean variables - Which is essencially 'True' or 'False'

raining = False

if raining:
    print("Stay Indoors!")
else:
    print("Go out you crazy fool!!!")



# You can flip this by using 'not' as a negative statement

raining = True

if not raining:
    print("Go outside, it's bloody lovely!")
else:
    print("It's pouring man, forget it!")