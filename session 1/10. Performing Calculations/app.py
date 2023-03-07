# Performing Calculations
# Mathmatical Operators
# Symbol    Operation           Description
# +         Addition            Adds two numbers
# -         Subtraction         Subtracts one number from another
# *         Multiplication      Multiplies one number by another
# /         Division            Divides one number by another and gives the result
#                               as a floating-point number.
# //        Integer Division    Divides one number by another and gives the result
#                               as a whole number (with decimal char. ex: 4.0).
# %         Remainder           Divides one number by another and gives the remainder
# **        Exponent            Raises a number to a power

# Floating-Point and Integer Division
# / - Floating point division
# // - Integer division

# Operator Precedence
# Python follows the same order of operations that you learned in math class.
# PEMDAS (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction)
# () - parentheses
# ** - exponents
# * or / or // or % (whichever comes first)
# + or - (whichever comes first)

result = 7.0 + 5.0 / 3.0 # outcome?

# Grouping with Parentheses
# ()

# The Exponent Operator
# **

# The Remainder Operator
# %

# Converting Math Formulas to Programming Statements

# What are the results of the following expressions?
# 5 + 2 * 4 = ?
# 10 / 2 - 3 = ?
# 8 + 12 * 2 - 4 = ?
# 6 - 3 * 2 + 7 - 1 = ?
# 2**3**4 = ?

# NOTE: There is an exception to the left-to-right rule. When two ** operators 
# share an operand, the operators execute right-to-left. For example, 
# the expression 2**3**4 is evaluated as 2**(3**4).


# Grouping with Parentheses
# Parts of a mathematical expression may be grouped with parentheses to force 
# some operations to be performed before others.
# (a * b) / 2 - what happens without the parentheses?

# What are the results of the following expressions?
# (5 + 2) * 4 = ?
# 10 / (2 - 3) = ?
# 8 + 12 * (2 - 4) = ?
# (6 - 3) * (2 + 7) - 1 = ?

# Excercises:
## 1. Convert Milliseconds to Hours, Minutes, and Seconds

## 2. Create a calculator

## 3. Calculating a Percentage
# If you are writing a program that works with a percentage, you have to make 
# sure that the percentage’s decimal point is in the correct location before 
# doing any math with the percentage. This is especially true when the user 
# enters a percentage as input. Most users enter the number 50 to mean 50 
# percent, 20 to mean 20 percent, and so forth. Before you perform any 
# calculations with such a percentage, you have to divide it by 100 to move its
# decimal point two places to the left. Let’s step through the process of 
# writing a program that calculates a percentage. Suppose a retail business is 
# planning to have a storewide sale where the prices of all items will be
# 20 percent off. We have been asked to write a program to calculate the sale 
# price of an item after the discount is subtracted. Here is the algorithm:
# 1. Get the original price of the item.
# 2. Calculate 20 percent of the original price. This is the amount of the discount.
# 3. Subtract the discount from the original price. This is the sale price.
# 4. Display the sale price.

## 4. Calculatin an Average
# Create 3 variables (a, b, and c) and ask the user to enter 3 numbers
# and place each number in one of the variables. Find the average and
# output the average to the console. Try it with and without using parentheses.
# Here is the algorithm:
# 1. Get the first number and store it in variable a
# 2. Get the second number and store it in variable b
# 3. Get the third number and store it in variable c
# 4. Calculate the average by adding the three values and dividing the sum
# by 3.
# 5. Display the average.