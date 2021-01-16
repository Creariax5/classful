import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
from flask import Flask
import imp
import glob
from os.path import dirname, basename, isfile, join

class WebServer:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.auth_token = None
        self.app = Flask(__name__)

    def load_routes_modules(self):

        routes_paths = ["routes/"]

        for routes_path in routes_paths:
            routes_modules = glob.glob(join(dirname(__file__), routes_path + "*.py"))
            [basename(f)[:-3] for f in routes_modules if isfile(f) and not f.endswith('__init__.py')]

            for module in routes_modules:
                loaded_module = imp.load_source('module.name', module)

                loaded_module.run(self)

    def run(self):
        self.load_routes_modules()
        self.app.run(port=self.port, host=self.host, debug=True)
