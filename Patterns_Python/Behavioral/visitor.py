class House(object):
    def accept(self, visitor):
        """Interface to accept a visitor"""
        visitor.visit(self)

    
