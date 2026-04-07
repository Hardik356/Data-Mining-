# print("Hellow Hardik")  # this is using a function print 

# official document for print statement is print(*objects, sep=" ", end="\n", file.sys.stdout, flush = False ) 
# here sep is seperate default is single space and end is default next line 
# and this can be overiable 

# functions 
# actions or verbers

# arguments 

# bugs is a mistake problems for u to solve 
# print("jvjf" this is a  bug a typo 

 # apple@apples-MacBook-Pro Python Course % python3 hello.py
#   File "/Users/apple/Documents/Python Course/hello.py", line 14
    
#     ^
# SyntaxError: unexpected EOF while parsing


# input takes a argument 
# input("What's Your Name ?")

# return values handed back to me the programmer could do somethig  with this 
# store it 

# variables like x, y in computers memory 

name = input("What's Your Name ?") # = sign is not equality this is a assignment operator from right to left 

# hands this value back to coder the container in computer memory is containing my name 

print("hello,")

print(name) # comments is notes to your code for techer or college to share the code 
# also sudo code express though and outline your code rigth comment sfor your self e.g


# ask the user for their name step 1
name_compact = input("Whats your name ?")


# say hello to usr step 2
print("Hello " + name_compact) # this require space + requires space single argumnets + 
# here we have positional parameters 
print("hello, ", name ) # this does no require any space this function use print with 2 arguments 

# adding the quotes inside the quotes 

print('heloo, "frnd"') # 1st way
print("hello, \"frind \"") # 2nd way 
print(f"heloo, {name_compact}")  # f {} this format string 

# str  this is the string sequient for characters 

# parameters 

# Remove clearing the white space for strings 

name_compact2 = input("Whats your name ?")

# remove the hitespace from the string

name_compact2 = name_compact2.strip() # = copy rigth to left after editing(removing the white space from the name input ) the string 

# Capitalize the name 
name_compact2 = name_compact2.capitalize() # this capitalize the first lettle only even for two waors only first eg hardiks ingla -> Hardik  singla

# title the name 
name_compact2 = name_compact2.title() # this capitalizr the first letle of both the lettle eg hardik singla Hardik Singla

# chaning the functions
# E.g strip.captalize or therefore input().strip().title() left to Right   Technical we can chain everything 

name_compact2 = name_compact2.strip().title()


# split function on string 
first , last = name_compact2.split()
print(f"hello", {first}) # this gives rigth to left eg hardik singla first -> hardik  


# Whats your name ? jlkl
# Traceback (most recent call last):
#   File "/Users/apple/Documents/Python Course/hello.py", line 80, in <module>
#     first , last = name_compact2.split()
# ValueError: not enough values to unpack (expected 2, got 1)

print(f"hello", {name_compact2})

















