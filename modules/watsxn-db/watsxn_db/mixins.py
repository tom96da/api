# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn DB Flask extension.
# (C) 2024 tom96da.com

""" watsxn_db.mixins module """

from datetime import datetime
from watsxn_db import db

class Timestamp:
    """
    A mixin class that provides timestamp columns for creation and update times.
    """
    created = db.Column(
        db.DateTime(timezone=False),
        default=datetime.now,
        nullable=False
    )
    """The timestamp for when the record was created."""

    updated = db.Column(
        db.DateTime(timezone=False),
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False
    )
    """The timestamp for when the record was last updated."""
