{% include navigation.html %}

# Data Structures Project

### [Python Coding Challenge Files in Github](https://github.com/katiehickman/katiehickman.github.io/tree/main/python_challenges)

### [Replit Menu](https://replit.com/@katiehickman270/katiehickmangithubio)

<center><iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@katiehickman270/katiehickmangithubio?lite=true"></iframe></center>


## Code Snippets 
### OOP LCM
```
# this class needs no init like the factorial because of no defined properties :)

class leastcm:
    def __call__(self, a, b):
        if (a > b):
            maximum = a
        else:
            maximum = b
        while (True):
            if (maximum % a == 0 and maximum % b == 0):
                break
            maximum = maximum + 1
        return maximum

def lcm_run():
    #first test
    a = 100
    b = 200
    lcm = leastcm()
    result = lcm(a,b)
    print("✨"*30, "\nThe LCM of", a, "and", b, "is", result)

    #second test
    a = 365
    b = 900
    result = lcm(a,b)
    print("✨"*30, "\nThe LCM of", a, "and", b, "is", result)

    #third test
    a = 20
    b = 10
    result = lcm(a,b)
    print("✨"*30, "\nThe LCM of", a, "and", b, "is", result)

```

### Imperative LCM
```
def findlcm(a,b):
    if (a > b):
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            break
        maximum = maximum + 1
    return maximum

def lcm():
    #first test
    print("✨"*30, "\nThe LCM of 100 and 150 is", findlcm(100,150))

    #second test
    print("✨"*30, "\nThe LCM of 25 and 60 is", findlcm(25,60))

    #third test
    print("✨"*30, "\nThe LCM of 5 and 15 is", findlcm(5,15))
```

### OOP Factorial
```
class factorial:
    def __init__(self):
        self.factorial = []

    def __call__(self,n):
        if n == 1 or n == 0:
            self.print()
            return 1
        else:
            self.factorial.append(n)
            return n * self(n-1)

    def print(self):
        print("✨"*30, "\nSequence: \n", *self.factorial)

def run_factorial():
    #first test
    n = 5
    facto = factorial()
    result = facto(n)
    print("✨"*30, "\nThe factorial of", n, "is", result)

    #second test
    n = 10
    facto = factorial()
    result = facto(n)
    print("✨"*30, "\nThe factorial of", n, "is", result)
```

### Imperative Factorial
```
# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester2():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
```

### Fibonacci 
```
def fibo(a):
    x = 0
    y = 1
    if a == 1:
        print(x)
    else:
        print(x)
        print(y)
    for i in range(2,a):
        z = x + y
        x = y
        y = z
        print(x+y)
fibo(100)
```

### InfoDB Loops
```
# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition
```

### InfoDB Lists
```
InfoDb Lists
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Katie",
    "LastName": "Hickman",
    "DOB": "December 27",
    "Residence": "San Diego",
    "Email": "katie.hickman2704@gmail.com",
    "Favorite_Animals":["Cat","Seal","Panther", "Polar Bear"]
})

InfoDb.append({
    "FirstName": "Nadira",
    "LastName": "Haddach",
    "DOB": "August 16",
    "Residence": "San Diego",
    "Email": "nadira@gmail.com",
    "Favorite_Animals":["Cat","Dog","Shark", "Seal"]
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Animals: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite_Animals"]))  # join allows printing a string list with separator
    print()

```

### Swap
```
def swap(age1, age2):
    temp = age1
    age1 = age2
    age2 = temp
    print("After Swap",(age1, age2))
number1 = int(input(" Please Enter the First number : "))
number2 = int(input(" Please Enter the Second number : "))
print("Before Swap",(number1, number2))
swap(number1, number2)
```

### Keypad
```
def keypad():
    print()
    numbers = ['1 2 3','4 5 6','7 8 9','  0  ']
    key_pad = '\n'.join(numbers)
    print(key_pad)
```

### Christmas Tree
```
def christmas():
    top = '🎀️'
    top_center = top.center(20, " ")
    print(top_center,end='')
    for i in range(10):
        star = '*' * (2*i)
        center_star = star.center(20, " ")
        print(center_star)
    print('        ||||')
    print('        ||||')
```

### Cat Animation
```
import time
import os

Color34 = "\u001b[34m"
Color37 = "\u001b[37m"

def cat1():
    print("|\---/|")
    print("| ,_, |")
    print(" \_`_/-..----.")
    print("___/ `   ' ,""+ \  ")
    print("(__...'   __\    |`.___.';")
    print("(_,...'(_,.`__)/'.....+")
    print("\u001b[34m -------------------------------------------- \u001b[37m")

def cat2():
    print("   |\---/|")
    print("   | ,_, |")
    print("    \_`_/-..----.")
    print("   ___/ `   ' ,""+ \  ")
    print("   (__...'   __\    |`.___.';")
    print("   (_,...'(_,.`__)/'.....+")
    print("\u001b[34m -------------------------------------------- \u001b[37m")

def cat3():
    print("      |\---/|")
    print("      | ,_, |")
    print("       \_`_/-..----.")
    print("      ___/ `   ' ,""+ \  ")
    print("      (__...'   __\    |`.___.';")
    print("      (_,...'(_,.`__)/'.....+")
    print("\u001b[34m -------------------------------------------- \u001b[37m")

def cat4():
    print("         |\---/|")
    print("         | ,_, |")
    print("          \_`_/-..----.")
    print("         ___/ `   ' ,""+ \  ")
    print("         (__...'   __\    |`.___.';")
    print("         (_,...'(_,.`__)/'.....+")
    print("\u001b[34m -------------------------------------------- \u001b[37m")

def cat5():
    print("            |\---/|")
    print("            | ,_, |")
    print("             \_`_/-..----.")
    print("            ___/ `   ' ,""+ \  ")
    print("            (__...'   __\    |`.___.';")
    print("            (_,...'(_,.`__)/'.....+")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


os.system("clear")
time.sleep(.1)
cat1()
time.sleep(.5)
os.system("clear")
cat2()
time.sleep(.5)
os.system("clear")
cat3()
time.sleep(.5)
os.system("clear")
cat4()
time.sleep(.5)
os.system("clear")
cat5()
time.sleep(.5)
os.system("clear")
```

### Ship Animation
```
#funcy.py
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    |\   ")
    print(sp + "    |/   ")
    print(SHIP_COLOR, end="")
    print(sp + "\__ |__/ ")
    print(sp + " \____/  ")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)
```
