# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn Flask application.
# (C) 2024 tom96da.com

""" WSGI module for the Watsxn Flask app.

This module creates the main Flask app instance and initializes the Watsxn
extensions.
"""

import os
from flask import Flask
from watsxn_base import WatsxnBase
from watsxn_db import WatsxnDB
from watsxn_trainup import WatsxnTrainup

def create_app():
    """ Create a new Flask app with the Watsxn extensions. """
    app_ = Flask(__name__)
    app_.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key')

    WatsxnBase(app_)
    WatsxnDB(app_)
    WatsxnTrainup(app_)

    return app_

app = create_app()
""" The main Flask app instance. """
