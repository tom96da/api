# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn DB Flask extension.
# (C) 2024 tom96da.com

""" watsxn_db.ext module

This module contains the WatsxnDB class which is used to initialize the
Watsxn DB extension for a Flask application.
"""

from flask import Flask

from . import config
from .cli import register_db_commands
from .shared import db

class WatsxnDB:
    """ The Watsxn DB Flask extension. """
    def __init__(self, app: Flask = None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """ Initialize the Watsxn DB extension for a Flask application. """
        app.logger.debug("WatsxnDB initialized")
        self.init_config(app)
        db.init_app(app)
        app.extensions["watsxn-db"] = self

    def init_config(self, app: Flask):
        """ Initialize the configuration options for the extension. """
        for k, v in config.__dict__.items():
            if k.startswith("WATSXN_DB_"):
                app.config.setdefault(k, v)
            if k.startswith("SQLALCHEMY_"):
                app.config.setdefault(k, v)

    def init_commands(self, app: Flask):
        """ Initialize the CLI commands for the extension. """
        register_db_commands(app)
