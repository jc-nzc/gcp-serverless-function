class Subject(object): #Represents what is being 'observed'

    def __init__(self):
        self._observers = [] #this is where references to all the observers are being kept
                             # Not that this is a one to many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
