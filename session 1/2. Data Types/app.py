# Dynamic vs. Statically typed languages

# Dynamically typed language:
# - Data types are determined at runtime, based on the value assigned to a variable.
# - No need to specify data types explicitly when declaring variables.
# - Variable types can change during runtime.
# - Code can be more concise and easier to read.
# - More flexible and forgiving, but potentially less efficient and 
# more prone to errors.

# Examples of statically typed languages include:
# Java
# C++
# C#
# Rust
# Go


# Statically typed language: 
# - Data types are determined at compile time, based on explicit type declarations.
# - Variables must be declared with specific data types.
# - Variable types cannot change during runtime.
# - Code can be more verbose and harder to read.
# - More rigid and less forgiving, but potentially more efficient and 
# less prone to errors.

# Examples of statically typed languages include:
# Python
# Ruby
# JavaScript
# PHP
# Perl


# Data Types:
# float: A data type used to represent decimal numbers with a fractional part. 
# Floating point numbers are stored in a binary format and can be subject to 
# rounding errors.
#
# int: A data type used to represent whole numbers (positive, negative, or zero) 
# without a fractional part.
#
# str: A data type used to represent strings of characters (text). Strings can 
# be enclosed in single quotes ('...') or double quotes ("...").
#
# bool: A data type used to represent Boolean values, which can be either True 
# or False. Boolean values are often used for logic and control flow in programs.
#
# list: A data type used to represent sequences of mutable (changeable) values, 
# enclosed in square brackets ([...]). Lists can contain elements of different 
# types, and their size can change dynamically.
#
# tuple: A data type used to represent sequences of immutable (unchangeable) 
# values, enclosed in parentheses ((...)). Tuples can contain elements of 
# different types, and their size is fixed.
#
# dict: A data type used to represent mappings between keys and values, enclosed 
# in curly braces ({...}). Dictionaries are unordered and mutable, and their 
# keys must be unique.
#
# These data types represent the basic building blocks of data in Python, and 
# each has its own unique properties and uses.


# The type function:
# The type() function is a built-in function in Python that returns the type 
# of a given object or value.


# Immutable & Mutable:
# Immutable: An immutable object is an object that cannot be modified after 
# it has been created. This means that any operation that would change the 
# value of the object creates a new object instead. Examples of immutable 
# objects in Python include integers, floats, strings, and tuples.
#
# Mutable: A mutable object, on the other hand, is an object that can be 
# modified after it has been created. This means that operations that modify 
# the object can be performed in place, without creating a new object. 
# Examples of mutable objects in Python include lists, dictionaries, and sets.
#
# Understanding the difference between immutable and mutable objects is 
# important in programming, as it can affect the behavior of your code. 
# For example, if you need to modify a collection of values frequently, using a 
# mutable data structure like a list might be more efficient than using an 
# immutable data structure like a tuple.



# Everything is an object?
# Yes, in Python, everything is an object. This means that everything in Python,
# including numbers, strings, functions, classes, and modules, is represented 
# as an object with a specific type and set of properties and methods.
