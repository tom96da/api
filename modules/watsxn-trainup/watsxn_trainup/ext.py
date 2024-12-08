from . import config
from .views import blueprint

class WatsxnTrainup:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.logger.debug("WatsxnTrainup initialized")
        self.init_config(app)
        app.register_blueprint(blueprint)
        app.extensions["watsxn-trainup"] = self

    def init_config(self, app):
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "WATSXN_TRAINUP_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"]
            )

        for k, v in config.__dict__.items():
            if k.startswith("WATSXN_TRAINUP_"):
                app.config.setdefault(k, v)
