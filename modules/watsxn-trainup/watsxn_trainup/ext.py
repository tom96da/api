# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn TrainUp Flask extension.
# (C) 2024 tom96da.com

""" watsxn_trainup.ext module

This module contains the WatsxnTrainup class which is used to initialize the
Watsxn TrainUp extension for a Flask application.
"""

from flask import Flask

from . import config
from .views import blueprint

class WatsxnTrainup:
    def __init__(self, app: Flask = None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.logger.debug("WatsxnTrainup initialized")
        self.init_config(app)
        app.register_blueprint(blueprint)
        app.extensions["watsxn-trainup"] = self

    def init_config(self, app: Flask):
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "WATSXN_TRAINUP_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"]
            )

        for k, v in config.__dict__.items():
            if k.startswith("WATSXN_TRAINUP_"):
                app.config.setdefault(k, v)
