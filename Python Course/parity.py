# +
# -
# *
# /
# %


def main():
    x = int(input("Enter the number ?"))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

def is_even(n):

    # best way is to return the condition if it has only boolen result ture / false 
    return n % 2 == 0

    # this is the like yeah Yeah yeah
    # return TRUE if n % 2 == 0 else False 

    # if n % 2 == 0:
    #     return True  # bool in python  
    # else:
    #     return False

main()

# x = int(input("Enter the number :"))

# if x%2==0:
#     print("EVEN")
# else:
#     print("ODD")