# Breaking Long Statements into Multiple Lines

# Statements & Expressions
# In programming, a statement is a line of code that performs a specific action, 
# such as assigning a value to a variable or calling a function. Statements are 
# executed one after the other, in order, and can sometimes have side effects on 
# the program's state or the values of variables.

# An expression, on the other hand, is a piece of code that produces a value. 
# Expressions can be used as part of a statement, or they can stand alone as 
# their own statement. For example, adding two numbers together is an expression 
# that produces a new value.

# In simpler terms, a statement is like a sentence that tells the computer to do 
# something, while an expression is like a phrase that produces a value. 
# While every statement in a program is made up of one or more expressions, 
# not every expression is a statement.

# Statements:
x = 5 # assigns the value 5 to the variable x
if x > 0: # begins an if statement block
    print("Hello, world!") # prints the string "Hello, world!" to the console

def my_function(x): # defines a function called "my_function"
    pass

# Expressions:
5 + 7 # adds the values 5 and 7 together, producing the value 12

"Hello" + " " + "world!" # concatenates the strings "Hello", " ", and "world!", 
# producing the value "Hello world!"

3 * (4 + 5) # multiplies the value 3 by the sum of 4 and 5, producing the value 27

my_list = [1, 2, 3]
my_list[2] # retrieves the third element from the list "my_list", producing a 
# value that depends on the contents of the list