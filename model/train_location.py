

class TrainLocation:

    def __init__(self, location, prefix, via):
        self._location = location
        self._prefix = prefix
        self._via = via

    def get_name(self):
        return self._location

    def get_prefix(self):
        return self._prefix

    def get_via(self):
        return self._via