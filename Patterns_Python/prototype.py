import copy

class Prototype:

    def __init__(self):
        self._object = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._object[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
