# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn Base Flask extension.
# (C) 2024 tom96da.com

""" watsxn_base.models module """

from flask_login import UserMixin

from watsxn_db import db
from watsxn_db.mixins import Timestamp

class User(db.Model, UserMixin, Timestamp):
    """ The User model.

    Attributes:
        id (int): The user ID.
        username (str): The username.
        password (str): The password.
        is_deleted (bool): The flag for soft deletion.
    """
    __tablename__ = "watsxn_users"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """The user ID."""

    username: str = db.Column(db.String(80), unique=True, nullable=False)
    """The username."""
    password: str = db.Column(db.String(80), nullable=False)
    """The password."""

    is_deleted: bool = db.Column(db.Boolean, nullable=False, default=False)
    """The flag for soft deletion."""

    def __repr__(self):
        return f"<User {self.username}>"

    @classmethod
    def count(cls, include_deleted: bool = False) -> int:
        """ Return the number of users.

        Args:
            include_deleted (bool): If True, include logically deleted records.

        Returns:
            int: The number of users.
        """
        if include_deleted:
            query = cls.query
        else:
            query = cls.query.filter_by(is_deleted=False)

        return query.count()

    @classmethod
    def create(cls, username: str, password: str) :
        """ Create a new user.

        Args:
            username (str): The username.
            password (str): The password.

        Returns:
            User: The newly created user.
        """
        user = cls(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user
