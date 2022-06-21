import functools

from zeep import Client
from zeep import xsd
from zeep.plugins import HistoryPlugin
import csv
import pandas as pd
import os
import requests

from model.station import *
from model.departure import *
from model.arrival import *


class Thameslink:
    WSDL = 'http://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01'
    station_url = 'https://www.nationalrail.co.uk/station_codes%20(07-12-2020).csv'
    stations = []

    def __init__(self, token):
        self._token = token

        self._history = HistoryPlugin()
        self._client = Client(wsdl=self.WSDL, plugins=[self._history])

        self._header = self.get_header()

        self.load_stations()
    def load_stations(self):

        if not os.path.exists("./stations.csv"):
            res = requests.get(self.station_url)
            f= open("stations.csv", "w")
            f.write(res.text)
            f.close()

        f = open("./stations.csv")
        csv_st = csv.reader(f)
        header = next(csv_st)
        unsorted_stations = []
        for r in csv_st:
            #print(r)
            for i in range(len(r)):
                if i%2==0 and len(r[i]) > 0:
                    station = Station(r[i+1], r[i])
                    unsorted_stations.append(station)
                    i += 1 #skip the next one because is NAME, PREFIX

        self.stations = sorted(unsorted_stations, key=functools.cmp_to_key(self.compare_station))

    def compare_station(self, s1, s2):
        if s1.get_name() > s2.get_name():
            return 1
        else:
            return -1

    def get_header(self):
        header = xsd.Element(
            '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}AccessToken',
            xsd.ComplexType([
                xsd.Element(
                    '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}TokenValue',
                    xsd.String()),
            ])
        )
        header_value = header(TokenValue=self._token)
        return header_value

    def get_client(self):
        return self._client

    def get_stations(self):
        return self.stations

    def get_departure_board(self, station):
        res = self._client.service.GetDepartureBoard(numRows=10, crs=station, _soapheaders=[self._header])
        departure = Departure(res)
        return departure

    def get_arrival_board(self, station):
        res = self._client.service.GetArrivalBoard(numRows=10, crs=station, _soapheaders=[self._header])
        arrival = Arrival(res)
        return arrival
