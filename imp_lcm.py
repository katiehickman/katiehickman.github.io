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
    print("The LCM of 100, 150 is", findlcm(100,150))

    #second test
    print("The LCM of 25, 60 is", findlcm(25,60))

    #third test
    print("The LCM of 5, 15 is", findlcm(5,15))