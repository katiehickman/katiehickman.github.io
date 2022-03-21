def swap(age1, age2):
    temp = age1 # temp is a temporary variable
    age1 = age2
    age2 = temp
    print("After Swap",(age1, age2)) # the actual swap
number1 = int(input(" Please Enter the First number : ")) # user input for the first number
number2 = int(input(" Please Enter the Second number : ")) # user input for the second number
print("Before Swap",(number1, number2)) # before the swap
swap(number1, number2) # runs the python function

#if __name__ == "__main__":
 #   swap()