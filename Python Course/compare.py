



# >
# >= 
# <=
# <
# == compare left to rigth 
# !=

# if is the keyword if ans is true then execute           slowest
x = int(input("Enter the vlaue of x"))

y = int(input("Enter the value of y"))

if x < y: # this boolean expresion do this or not this 
    print("X is less then Y")
if x > y:
    print("X is Greater than Y")
if x == y:
    print("X is equal to Y")

# elif is the keyword used if and is true then pirnt else go to next  faster than if 

if x < y: # this boolean expresion do this or not this 
    print("X is less then Y")
elif x > y:
    print("X is Greater than Y")
elif x == y:
    print("X is equal to Y")


# else is the keyword used dead condition last result fastest 

if x < y: # this boolean expresion do this or not this 
    print("X is less then Y")
elif x > y:
    print("X is Greater than Y")
else:
    print("X is equal to Y")


# or keyword compare 1 - 0  = 1 / 0 - 1  = 1  

if x < y or y > x:
    print("X is not equal to Y")     
else:
    print("X is equal to Y")

    # now this is the impeoment should ask less question tighter the conditions 
if x == y:        # x!=y can also be used just opposite the print statements ****
    print("X is equal to Y")
else:
    print("X is not equal to Y")
