class Handler:
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)


        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in sublass!')
