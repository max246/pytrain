import configparser
from lib.thameslink import *

config = configparser.ConfigParser()
config.read("config.ini")

token = config.get("main", "token")
tl = Thameslink(token)

'''stations = tl.get_stations()
station = stations[0]
r = tl.get_departure_board(station.get_prefix())
rs = r.get_services()
print("Service from ", station.get_name())
rs[0].print()
'''
r = tl.get_arrival_board('SAC')
rs = r.get_services()
rs[0].print()