

class TrainService:

    def __init__(self, time, status, operator, platform, origin, destination):
        self._time = time
        self._status = status
        self._operator = operator
        self._platform = platform
        self._origin = origin
        self._destination = destination

    def get_time(self):
        return self._time

    def get_status(self):
        return self._status

    def get_operator(self):
        return self._operator

    def get_origin(self):
        return self._origin

    def get_destination(self):
        return self._destination

    def get_platform(self):
        return self._platform

    def print(self):
        print("Train origin from ", self._origin.get_name(), " at ",self._time , " is ",self._status, " to ", self._destination.get_name(), " on platform ", self._platform, "operated by ",self._operator)