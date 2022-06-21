import configparser
from flask import Flask
from flask_cors import CORS
from lib.api import *

config = configparser.ConfigParser()
config.read("config.ini")


app = Flask(__name__)
app.config['TOKEN_LDBWS'] = config.get("main", "token")
app.config['TRAIN'] =  Thameslink(app.config['TOKEN_LDBWS'] )


r = app.config['TRAIN'].get_arrival_board('SAC')
rs = r.get_services()
rs[0].print()
CORS(app)

app.register_blueprint(api)

def main():
    app.run(host='0.0.0.0', debug=False, port=5050)

if __name__ == '__main__':
    main()