#-------------------------------------------------------
#  Title: davidson_calculator.py
#  Author: John Davidson
#  Date: 26 August 2023
#  Description: Exercise 3.3 for WEB 335 - Intro to NoSQL.
#-------------------------------------------------------

# Define a function that adds two numbers.
def add(num1, num2):
  return (num1 + num2)

# Define a function that subtracts two numbers.
def subtract(num1, num2):
  return(num1 - num2)

# Define a function that divides two numbers.
def divide(num1, num2):
  return(num1 / num2)

# Define a function that multiplies two numbers.
def multiply(num1, num2):
  return(num1 * num2)

# Define two variables to test functions
x = 10
y = 20

add_string = f"{x} + {x} is {add(x, x)}" # Displays the results of the add calculation in string format.

subtract_string = f"{y} - {x} is {subtract(y, x)}" # Displays the results of the subtract calculation in string format.

divide_string = f"{y} / {x} is {divide(y, x)}" # Displays the results of the divide calculation in string format.

multiply_string = f"{x} * {x} is {multiply(x, x)}" # Displays the results of the multiply calculation in string format.

# Print every calculation string to the console.
print(add_string)
print(subtract_string)
print(divide_string)
print(multiply_string)

