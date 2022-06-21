from model.train_service import *
from model.train_location import *


class Arrival:

    def __init__(self, raw_data):
        self._services = []
        self.parse_data(raw_data)

    def parse_data(self, data):
        self._station = data.locationName
        self._station_prefix = data.crs

        services = data.trainServices.service

        for service in services:
            origin_train = self.parse_location(service.origin.location)
            destination_train = self.parse_location(service.destination.location)
            s = TrainService(service.sta, service.eta, service.operator,  service.platform, origin_train, destination_train)
            self._services.append(s)

    def parse_location(self, locations):
        if len(locations) > 0:
            location = TrainLocation(locations[0].locationName, locations[0].crs, locations[0].via)
            return location
        else:
            return None

    def get_station_name(self):
        return self._station

    def get_station_prefix(self):
        return self._station_prefix

    def get_services(self):
        return self._services
