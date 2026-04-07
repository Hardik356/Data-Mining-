# while True:
#     n = int(input("Enter the value of n"))
#     if n > 0 :
#         break

# for _ in range(n):
#     print("meow")




# # while continous 
# i = 3
# while i != 0:
#     print("meow") 
#     i = i - 1 # decriment 


# i = 0
# while i < 3:
#     print("meow") 
#     i += 1 # increament  rigth to left assignment 


# # for condition 
#     # list datatypes is the list of things in python muplile values 

# for i in [0,1,2]:
#     print("meow")

# for i in range(3): # this return the range from 0,1,2
#     print("meow")

# # special case  
# print("meow\n" * 3, end="")  





def main():
    meow(get_number())

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    n = int(input("Enter the value "))
    if n > 0:
        return n

main()