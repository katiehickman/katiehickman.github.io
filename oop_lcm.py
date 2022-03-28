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
