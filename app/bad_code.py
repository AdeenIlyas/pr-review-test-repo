# bad_code.py

import math      # UNUSED import
import os        # UNUSED import
import sys       # UNUSED import


# BAD naming: class name should be CamelCase
class bad_class:
    def __init__(self):
        self.x = 10

    # BAD naming: function name should be snake_case
    def PrintMessage(self, msg):
        print(msg)

    # BAD naming: variable 'y' is too short / non‑descriptive
    def calculate(self, y):
        z = y * 2
        return z


# BAD naming: function name should be snake_case
def ThisIsABadFunctionName():
    unused_variable = 42      # UNUSED variable
    another_unused = "hello"  # UNUSED variable
    return True


# MODULARITY issue: very long function with deep nesting
def very_long_function():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    if a > b:
        if c > d:
            if e > f:
                if g > h:
                    if i > j:
                        print("Nested too deep!")
    return a + b + c + d + e + f + g + h + i + j


# MODULARITY issue: too many arguments (bad design)
def too_many_arguments(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j


# UNUSED function (dead code)
def unused_function():
    print("I am never called!")


# UNUSED class (dead code)
class UnusedClass:
    pass