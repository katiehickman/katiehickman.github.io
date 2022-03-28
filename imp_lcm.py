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