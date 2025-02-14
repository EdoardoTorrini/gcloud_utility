from flask import Flask
from flask_cors import CORS
from flask_classful import FlaskView

from views.view_api import ViewAPI
from views.view_web import ViewWeb

from models.model import Model

app = Flask(__name__)
cors = CORS(app)

# need to change the name of the collection based on the one that it is create
users = Model("utenti")

ViewWeb.register(app, init_argument=users, route_base="/")
ViewAPI.register(app, init_argument=users, route_base="/api/v0.1/view")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4242, debug=True)