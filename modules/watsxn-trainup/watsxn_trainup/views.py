# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn TrainUp Flask extension.
# (C) 2024 tom96da.com

""" watsxn_trainup.views module

This module contains the views for the Watsxn TrainUp extension.
"""

from flask import Blueprint, request, current_app

blueprint = Blueprint("watsxn_trainup", __name__, url_prefix="/trainup")

@blueprint.route("/")
def index():
    current_app.logger.debug("TrainUp index page")
    return "<h1>Watsxn TrainUp</h1>"
