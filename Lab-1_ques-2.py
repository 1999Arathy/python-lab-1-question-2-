#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

user_input = int(input("enter a number"))
if(user_input %2 ==0):
    print("User input is an even number")
else:
    print("User input is an odd number")
