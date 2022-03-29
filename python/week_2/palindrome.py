import re


class Palindrome:
  def __call__(self, n):
    n = re.sub(r'[^a-zA-Z0-9]', '', n).lower()
    if n == n[::-1]:
      # If the original thing is equal to its reverse
      return " "
      # Is a palindrome
    else:
      return " not "
      #Is not a palindrome
  
def test():
  pal = Palindrome()
  n = "is this a palindrome"
  print(f'"{n}" is' + pal(n) + "a palindrome")
  # testing if "is this a palindrome" is a palindrome
  n = "taco cat"
  print(f'"{n}" is' + pal(n) + "a palindrome")
  # testing if "tacocat" is a palindrome
  n = "Sit on a potato pan, Otis."
  print(f'"{n}" is' + pal(n) + "a palindrome")
  # testing if "Sit on a potato pan, Otis." is a palindrome
  n = "racecar"
  print(f'"{n}" is' + pal(n) + "a palindrome")
  # testing if "racecar" is a palindrome
  n = "hello"
  print(f'"{n}" is' + pal(n) + "a palindrome")
  # testing if "hello" is a palindrome
  n = "this is not a palindrome"
  print(f'"{n}" is' + pal(n) + "a palindrome")
  # testing if "this is not a palindrome" is a palindrome
  
def run():
  pal = Palindrome()
  try:
    n = input("Enter your string ")
    print(f'"{n}" is' + pal(n) + "a palindrome")
    #
  except:
    print("string")