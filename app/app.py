from flask_migrate import Migrate
from main import create_app, db
from main.controller.admin_route import admin
from main.controller.gsm_cell import cell
from main.controller.location import location
from main.controller.wifi_network import wifi

app = create_app()

migrate = Migrate(app, db)

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(cell, url_prefix="/celltower")
app.register_blueprint(wifi, url_prefix="/wifi")
app.register_blueprint(location, url_prefix="/location")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
