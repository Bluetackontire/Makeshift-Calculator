##from datetime import datetime
##
##now = datetime.now()
##current_time = now.strftime("%H:%M:%S")
##print("Current Time =", current_time)

from functions import add, minus, times, divide, quadratic

while True:
    print("=" * 45)
    choice = {"1": "addition",
              "2": "subtraction",
              "3": "multiplication",
              "4": "division",
              "5": "quadratic formula (when ax²+bx+c = 0)",
              "0": "quit"
              }


    for key, value in choice.items():
        print(key, ' : ', value)

    decision = int(input("Please enter the number you want to choose: "))

    if decision == 0:
        print("Thank you for your time")
        break
    elif decision not in range(1,6):
        print("Please try again")
    elif decision != 5:
        x = float(input("Enter a number: "))
        y = float(input("Enter a number: "))

    if decision == 1:
        sums = add(x,y)
        print("The sum is", sums)
    
    if decision == 2:
        sub = minus(x,y)
        print("The subtraction is", sub)
    
    elif decision == 3:
        product = times(x,y)
        print("The product is", product)
    
    if decision == 4:
        div = divide(x,y)
        print("The division is", div)
        
    if decision == 5:
      a = int(input("Enter a: "))
      b = int(input("Enter b: "))
      c = int(input("Enter c: "))
      print(quadratic(a,b,c))