from functools import wraps

def make_blink(function):
    """Defines the decorator"""

    #This makes the decorator transparent in terms of its name and docstring
