# Calculator Program

"""
This program provides the user with the ability to do calculations just like a calculator.  It can do addition, subtraction, multiplication, and division.  It also has the ability to work with decimals.

In the future I can improve this calculator by allowing for more complex calculations and creating a user interface to interact with.  Right now I don't have the skills to create a UI.
"""

from art import logo
print(logo)

# Addition
def add(n1, n2):
  return n1 + n2

# Subtraction
def subtract(n1, n2):
  return n1 - n2

# Multiplication
def multiply(n1, n2):
  return n1 * n2

# Division
def divide(n1, n2):
  return n1 / n2
# -------------------------------------------------------------------------
n1 = float(input("What is the first number?: "))

mathoperations = ["+", "-", "*", "/"]
for x in mathoperations:
  print(x)

operation = input("Which operation do you want to calculate?  Select one of the above: ")
n2 = float(input("What is the second number?: "))
# ------------------------------------------------------------
def calculation(number1, operation, number2):
  if operation == mathoperations[0]:
    sum = add(number1, number2)
    print(f"{number1} + {number2} = {sum}")
    return sum
    
  elif operation == mathoperations[1]:
    difference = subtract(number1, number2)
    print(f"{number1} - {number2} = {difference}")
    return difference
    
  elif operation == mathoperations[2]:
    product = multiply(number1, number2)
    print(f"{number1} * {number2} = {product}")
    return product
    
  elif operation == mathoperations[3]:
    quotient = divide(number1, number2)
    print(f"{number1} / {number2} = {quotient}")
    return quotient
    
answer = calculation(n1, operation, n2)
# -------------------------------------------------------------
continue_calc = input(f"Type 'y' to continue calculating with {answer}.  Type 'n' to stop. ").lower()

if continue_calc == "y":
  runprogram = True
elif continue_calc == "n":
  runprogram = False
  print("This is the end of the program.  Thank you.")

while runprogram == True:
  for x in mathoperations:
    print(x)

  operation = input("Which operation do you want to calculate?  Select one of the above: ")

  n3 = float(input("OK, enter the next number. "))

  answer = calculation(answer, operation, n3)

  continue_calc = input(f"Type 'y' to continue calculating with {answer}. Type 'n' to stop. ").lower()

  if continue_calc == "y":
    runprogram = True
  elif continue_calc == "n":
    runprogram = False
    print("This is the end of the program.  Thank you.")