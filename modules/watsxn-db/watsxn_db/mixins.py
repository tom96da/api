# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn DB Flask extension.
# (C) 2024 tom96da.com

""" watsxn_db.mixins module """

from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr

class Timestamp:
    """
    A mixin class that provides timestamp columns for creation and update times in JST (Japan Standard Time).
    """
    @staticmethod
    def current_time_jst():
        return datetime.now(ZoneInfo('Asia/Tokyo'))

    @declared_attr
    def created(cls):
        return Column(DateTime(timezone=True), default=cls.current_time_jst)

    @declared_attr
    def updated(cls):
        return Column(DateTime(timezone=True), default=cls.current_time_jst, onupdate=cls.current_time_jst)
