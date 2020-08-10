import time

class Producer:
    """Define the 'resource-intensive' object to instantiate!"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None
    
