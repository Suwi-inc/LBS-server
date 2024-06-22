from flask_migrate import Migrate
from main import create_app, db
from main.controller.admin_route import admin
from main.controller.device_route import device
from main.controller.gsm_cell import cell
from main.controller.location import location
from main.controller.wifi_network import wifi

app = create_app()
app.debug = True
app.url_map.strict_slashes = False
migrate = Migrate(app, db)

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(device, url_prefix="/device")
app.register_blueprint(cell, url_prefix="/celltower")
app.register_blueprint(wifi, url_prefix="/wifi")
app.register_blueprint(location, url_prefix="/location")


# for tests, got to be delete later
@app.route("/")
def hello_world():
    return "Hello, World!"


# deleted later

if __name__ == "__main__":
    app.run()
