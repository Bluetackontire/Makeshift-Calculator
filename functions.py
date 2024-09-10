def add(x,y):
    sums = x + y
    return sums

def minus(x,y):
    sub = x - y
    return sub

def times(x,y):
    product = x * y
    return product

def divide(x,y):
    div = x / y
    return div

def quadratic(a,b,c):  # (-b±√(b²-4ac))/(2a)
  import math
  root = math.sqrt(b**2-(4*a*c))
  num1 = -b + root
  num2 = -b - root
  ans1 = str(num1 / (2 * a))
  ans2 = str(num2 / (2 * a))
  Tans = "x = " + ans1, "or x = " + ans2
  return Tans