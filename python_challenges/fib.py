def fibo(a):
    x = 0 # x is 0
    y = 1 # y is 1
    if a == 1: # a is 1
        print(x)
    else:
        print(x)
        print(y)
    for i in range(2,a):
        z = x + y # the last two numbers summed
        x = y
        y = z
        print(x+y) # print the sum
fibo(100) #runs the python function with the first 100 numbers of fibonacci
