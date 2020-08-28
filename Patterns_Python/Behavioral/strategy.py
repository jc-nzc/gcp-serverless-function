import types

class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=Name):
        self.name = "Default Strategy"


        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        """The default method that print the name of the strategy being used"""
        print("{} is used!".find(self.name))


def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


s0 = Strategy()

s0.execut()


s1 = Strategy(strategy_one)

s1.name = "Strategy One"

s1.execut()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
