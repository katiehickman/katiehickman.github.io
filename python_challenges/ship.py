import time
import os

Color34 = "\u001b[34m"
Color37 = "\u001b[37m"


# As you can see, its not very optimal
def ship1():
    print("    |\ ")
    print("    |/ ")
    print("\__ |__/ ")
    print(" \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship2():
    print("      |\ ")
    print("      |/ ")
    print("  \__ |__/ ")
    print("   \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship3():
    print("        |\ ")
    print("        |/ ")
    print("    \__ |__/ ")
    print("     \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship4():
    print("          |\ ")
    print("          |/ ")
    print("      \__ |__/ ")
    print("       \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship5():
    print("            |\ ")
    print("            |/ ")
    print("        \__ |__/ ")
    print("         \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship6():
    print("              |\ ")
    print("              |/ ")
    print("          \__ |__/ ")
    print("           \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship7():
    print("                |\ ")
    print("                |/ ")
    print("            \__ |__/ ")
    print("             \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship8():
    print("                  |\ ")
    print("                  |/ ")
    print("              \__ |__/ ")
    print("               \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship9():
    print("                    |\ ")
    print("                    |/ ")
    print("                \__ |__/ ")
    print("                 \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship10():
    print("                      |\ ")
    print("                      |/ ")
    print("                  \__ |__/ ")
    print("                   \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship11():
    print("                        |\ ")
    print("                        |/ ")
    print("                    \__ |__/ ")
    print("                     \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship12():
    print("                          |\ ")
    print("                          |/ ")
    print("                      \__ |__/ ")
    print("                       \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship13():
    print("                            |\ ")
    print("                            |/ ")
    print("                        \__ |__/ ")
    print("                         \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship14():
    print("                              |\ ")
    print("                              |/ ")
    print("                          \__ |__/ ")
    print("                           \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship15():
    print("                                |\ ")
    print("                                |/ ")
    print("                            \__ |__/ ")
    print("                             \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship16():
    print("                                  |\ ")
    print("                                  |/ ")
    print("                              \__ |__/ ")
    print("                               \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship17():
    print("                                    |\ ")
    print("                                    |/ ")
    print("                                \__ |__/ ")
    print("                                 \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship18():
    print("                                      |\ ")
    print("                                      |/ ")
    print("                                  \__ |__/ ")
    print("                                   \____/ ")
    print("\u001b[34m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \u001b[37m")


def ship19():
    print("                                        |\ ")
    print("                                        |/ ")
    print("                                    \__ |__/ ")
    print("                                     \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


def ship20():
    print("                                          |\ ")
    print("                                          |/ ")
    print("                                      \__ |__/ ")
    print("                                       \____/ ")
    print("\u001b[34m -------------------------------------------- \u001b[37m")


os.system("clear")
time.sleep(.1)
ship1()
time.sleep(.5)
os.system("clear")
ship2()
time.sleep(.5)
os.system("clear")
ship3()
time.sleep(.5)
os.system("clear")
ship4()
time.sleep(.5)
os.system("clear")
ship5()
time.sleep(.5)
os.system("clear")
ship6()
time.sleep(.5)
os.system("clear")
ship7()
time.sleep(.5)
os.system("clear")
ship8()
time.sleep(.5)
os.system("clear")
ship9()
time.sleep(.5)
os.system("clear")
ship10()
time.sleep(.5)
os.system("clear")
ship11()
time.sleep(.5)
os.system("clear")
ship12()
time.sleep(.5)
os.system("clear")
ship13()
time.sleep(.5)
os.system("clear")
ship14()
time.sleep(.5)
os.system("clear")
ship15()
time.sleep(.5)
os.system("clear")
ship16()
time.sleep(.5)
os.system("clear")
ship17()
time.sleep(.5)
os.system("clear")
ship18()
time.sleep(.5)
os.system("clear")
ship19()
time.sleep(.5)
os.system("clear")
ship20()
time.sleep(.5)
os.system("clear")
print("or so you thought...")
time.sleep(.5)
os.system("clr")

#faster way
#import time

# terminal print commands
#ANSI_CLEAR_SCREEN = u"\u001B[2J"
#ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
#OCEAN_COLOR = u"\u001B[44m\u001B[2D"
#SHIP_COLOR = u"\u001B[32m\u001B[2D"
#RESET_COLOR = u"\u001B[0m\u001B[2D"

#def ocean_print():
    # print ocean
 #   print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
 #   print("\n\n\n\n")
 #   print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
#def ship_print(position):
  #  print(ANSI_HOME_CURSOR)
  #  print(RESET_COLOR)
  #  sp = " " * position
  #  print(sp + "    |\   ")
  #  print(sp + "    |/   ")
  #  print(SHIP_COLOR, end="")
  #  print(sp + "\__ |__/ ")
   # print(sp + " \____/  ")
  #  print(RESET_COLOR)


# ship function, iterface into this file
#def ship():
    # only need to print ocean once
  #  ocean_print()

    # loop control variables
  #  start = 0  # start at zero
  #  distance = 60  # how many times to repeat
  #  step = 2  # count by 2

    # loop purpose is to animate ship sailing
  # for position in range(start, distance, step):
   #     ship_print(position)  # call to function with parameter
   #     time.sleep(.1)