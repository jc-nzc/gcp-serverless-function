class Component(object):
    """ Abstract clas """

    def __init(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component):
    """Concrete class"""

    def __init__(self, *args, *kwargs):
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        #Print the name of your child item here!
        print("{}".format(self.name))

class Composite(Component): #Inherits from the abstract class, Component
    """Concrete class and maintains the tree resursive structure"""
