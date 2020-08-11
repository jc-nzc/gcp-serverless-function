class Subject(object): #Represents what is being 'observed'

    def __init__(self):
        self._observers = [] #this is where references to all the observers are being kept
                             # Not that this is a one to many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):

    def __init__(self, name-""):
        Subject._name = name
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()

class TempViewer:

    def update(self, subject):
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))
