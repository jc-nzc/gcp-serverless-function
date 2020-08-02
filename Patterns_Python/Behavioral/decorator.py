from functools import wraps

def make_blink(function):
    """Defines the decorator"""

    #This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    #Define the inner function
    def decorator():
        #Grab the return value of the function being decorated
        ret = function()

        #Add new functionality to the function being decorate
        return "<blink>" + ret + "</blink>"

    return decorator
