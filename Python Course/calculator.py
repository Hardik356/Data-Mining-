# return function values 
def main():
    x = int(input("Enter the value :"))

    print("x squared x is", square(x))

def square(x):
    return x*x
    # return x**2 raise the power to left given
    # return pow(x,2) raise the power using function

main()







 # int is a datype and a function 
x = int(input("Enter the value for x ")) # we can wrap the input function with data type # 
# Enter the value for x r
# Traceback (most recent call last):
#   File "/Users/apple/Documents/Python Course/calculator.py", line 3, in <module>
#     x = int(input("Enter the value for x ")) # we can wrap the input function with data type 
# ValueError: invalid literal for int() with base 10: 'r'

y = int(input("Enter the value for y ")) 


print(x+y)



# print(int(input("Enter the value for x ")) + int(input("Enter the value for y ")) ) # this is too much 


x = float(input("Enter the value for x "))
y = float(input("Enter the value for y ")) # float cannot increase too much memory is 

# round the result could be done using round(number[, ndigits]) here [] means something is optional e.g if we does so only int if 1 ,2 then to th=enths , hunders place 

print(x+y)

# just a criptic way to format the answer could be -> print (f{x+y:,}) this will format the result into comma sepearated us one eg 999+1 = 1,000

# division 

x = float(input("Enter the value for x "))
y = float(input("Enter the value for y ")) 

# z = round(x / y ,2)
z = x/y

print(f"{z:.2f}")



