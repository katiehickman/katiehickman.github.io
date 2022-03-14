#def swapnumbers(age1, age2):
  #  if age1 > age2:
 #       temp = age1
 #      age1 = age2
 #       age2 = temp
  #  return age1, age2

def swap_input():
    list = []
    age1 = input("Enter the first number:")
    age2 = input("Enter the second number:")
    def swap(num1, num2):
        if age1 > age2:
            list.append(age2)
            list.append(age1)
        if age1 < age2:
            list.append(age1)
            list.append(age2)
    swap(age1,age2)
    print("result", list)