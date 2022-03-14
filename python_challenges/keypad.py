#def keypad(keypad):
 #   print("keypad!")
 #   for i in range(len(keypad)):
 #       for j in range(len(keypad[i])):
 #           print(keypad[i][j], end="")
#        print()

def keypad():
    print()
    numbers = ['1 2 3','4 5 6','7 8 9','  0  ']
    key_pad = '\n'.join(numbers)
    print(key_pad)