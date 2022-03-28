# imports
from python.week_1 import lists
from python.week_2 import imp_lcm, oop_lcm, oop_fact

# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu1 = [
    ["Swap", "python/week_0/swap.py"],
    ["Keypad", "python/week_0/keypad.py"],
    ["Christmas Tree", "python/week_0/christmas.py"],
    ["Loops", lists.tester1],

]

sub_menu2 = [
    ["Cat", "python/week_0/cat.py"],
    ["Ship", "python/week_0/ship.py"],

]

sub_menu3 = [
    ["100 Fibonacci", "python/week_1/fib.py"],
    ["Factorial", lists.tester2],
    ["OOP Factorial", oop_fact.run_factorial],
    ["OOP LCM", oop_lcm.lcm_run],
    ["Imperative LCM", imp_lcm.lcm],

]
# Menu banner is typically defined by menu owner
border = "\033[32m=\033[36m" * 25
banner = f"\033[37m\n{border}\nPlease Pick An Option!\n{border}\033[37m"
# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "\033[36mFunction Menu\033[36m" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Fun Functions", submenu1])
    menu_list.append(["Animations", submenu2])
    menu_list.append(["Math", submenu3])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu1():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu1)

def submenu2():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu2)

def submenu3():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu3)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])
    # get user choice
    choice = input("\033[36mInput:\033[36m")
    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            print("You have exited the program!")
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try
    buildMenu(banner, options)  # recursion, start menu over again
if __name__ == "__main__":
    menu()