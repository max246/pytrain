from flask import Blueprint, request,abort,jsonify, current_app
from lib.thameslink import *

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def home():
    tl = current_app.config['TRAIN']
    return "home"

@api.route('/stations', methods=['GET'])
def statiosn():
    tl = current_app.config['TRAIN']
    stations = tl.get_stations()
    ouptut = []
    for station in stations:
        ouptut.append({"name": station.get_name(), "prefix": station.get_prefix()})
    return jsonify(ouptut)

@api.route('/departure', methods=['POST'])
def departure():
    data = request.get_json()
    station_prefix = data['prefix']
    tl = current_app.config['TRAIN']

    result = tl.get_departure_board(station_prefix)
    services = result.get_services()

    output = []
    for service in services:
        output.append({"time" : service.get_time(),
                       "status": service.get_status(),
                       "operator": service.get_operator(),
                       "origin" : service.get_origin(),
                       "destination": service.get_destination(),
                       "platform":service.get_platform()})
    return jsonify(output)

'''stations = tl.get_stations()
station = stations[0]
r = tl.get_departure_board(station.get_prefix())
rs = r.get_services()
print("Service from ", station.get_name())
rs[0].print()

r = tl.get_arrival_board('SAC')
rs = r.get_services()
rs[0].print()
'''