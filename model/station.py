

class Station:

    def __init__(self, prefix, name):
        self._prefix = prefix
        self._name = name

    def get_prefix(self):
        return self._prefix

    def get_name(self):
        return self._name
