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
