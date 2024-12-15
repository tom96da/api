# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn Base Flask extension.
# (C) 2024 tom96da.com

""" watsxn_base.ext module

This module contains the WatsxnBase class which is used to initialize the
Watsxn Base extension for a Flask application.
"""

from flask import Flask
from flask_bcrypt import Bcrypt

from . import config
from .views import blueprint, login_manager

class WatsxnBase:
    """ The Watsxn Base Flask extension. """
    def __init__(self, app: Flask = None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """ Initialize the Watsxn Base extension for a Flask application. """
        app.logger.debug("WatsxnBase initialized")
        app.extensions["bcrypt"] = Bcrypt(app)
        # login_manager = LoginManager(app)
        # login_manager.login_view = "watsxn_base.login"
        login_manager.init_app(app)

        self.init_config(app)
        app.register_blueprint(blueprint)
        app.extensions["watsxn-base"] = self

    def init_config(self, app: Flask):
        """ Initialize the configuration options for the extension. """
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "WATSXN_BASE_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"]
            )

        for k, v in config.__dict__.items():
            if k.startswith("WATSXN_BASE_"):
                app.config.setdefault(k, v)
