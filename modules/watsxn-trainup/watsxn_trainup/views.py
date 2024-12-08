from flask import Blueprint, request, current_app

blueprint = Blueprint("trainup", __name__, url_prefix="/trainup")

@blueprint.route("/")
def index():
    current_app.logger.debug("Trainup index page")
    return "<h1>Watsxn Trainup</h1>"









