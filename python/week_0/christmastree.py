def tree(n, p):
  z = n - 1
  x = 1
  for i in range(0, n):
    print(' ' * z, f'{p} ' * x, ' ' * (z - 1))
    x += 1
    z -= 1
  if n // 3 % 2 == 1:
    y = n // 3 + 2
  else:
    y = n // 3 + 1
  for i in range (0, y - 1):
    print(' ' * (n - ((y - 1) //2 + 1)), f'{p}' * y, ' ' * (n - ((y - 1) //2 + 1)))


def options():
  try:
    n = int(input("How tall do you want the Christmas tree?\n"))
    p = input("What character should be used to build the tree?\n")
    tree(n, p)
  except:
    print("bad choice bro")
