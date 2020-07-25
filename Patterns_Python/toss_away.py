class Borg:
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data

class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)

x = Singleton(AJAX="Asynchronus Javascript and XML")
print(x)

y = Singleton(JSON="Javascript Object Notation")
print(y)

z = Singleton(JAC="John Albert Chorus")
print(z)
