# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn DB Flask extension.
# (C) 2024 tom96da.com

""" watsxn_db.shared module

This module contains shared database objects for the Watsxn DB extension.
"""

from sqlalchemy import MetaData, util
from flask_sqlalchemy import SQLAlchemy

NAMING_CONVENTION = util.immutabledict({
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
})
"""Configuration for constraint naming conventions."""

metadata = MetaData(naming_convention=NAMING_CONVENTION)
"""Default database metadata object holding associated schema constructs."""


db = SQLAlchemy(metadata=metadata)
"""Shared database instance using Flask-SQLAlchemy extension."""
