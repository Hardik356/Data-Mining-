def main():
    name  = input("Whats your name ? ")
    hello(name) # variable is passed to function eg name stores passes in to hello to parameter 

def hello(to="world"): # : means stay tune for intendation    to is the parameter  also define the function before calling 
    print("Hello," , to)

main()
# hello() # top to bottom approch i.e to="world default value when run this has the value "
# name  = input("Whats your name ? ")
# hello(name) # variable is passed to function eg name stores passes in to hello to parameter 


# scope of the varibale is like the same 
# def main():
#     name  = input("Whats your name ? ")
#     hello() # variable is passed to function eg name stores passes in to hello to parameter 
# def hello(): # : means stay tune for intendation    to is the parameter  also define the function before calling 
#     print("Hello," , name)
# main() this wil give error ameError: name 'name' is not defined
