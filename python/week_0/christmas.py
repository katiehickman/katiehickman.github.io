def christmas():
    top = '🎀️' # top of the tree
    top_center = top.center(20, " ")
    print(top_center,end='')
    for i in range(10): # base
        star = '*' * (2*i)
        center_star = star.center(20, " ")
        print(center_star)
    print('        ||||')
    print('        ||||') # base of the treee
christmas() # runs the python function

# if __name__ == "__main__":
 #   christmas()