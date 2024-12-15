# -*- coding: utf-8 -*-
#
# This file is part of the Watsxn Base Flask extension.
# (C) 2024 tom96da.com

""" watsxn_base.views module """

from flask import (
    Blueprint, flash, redirect, render_template, request, current_app, url_for
)
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user
)
from flask_bcrypt import Bcrypt

from watsxn_base.models import User


blueprint = Blueprint("watsxn_base", __name__, template_folder="templates")
login_manager = LoginManager()
login_manager.login_view = "watsxn_base.login"


@login_manager.user_loader
def load_user(user_id) -> User:
    """ Loads a user from the database by their user ID.

    Args:
        user_id (int): The ID of the user to load.

    Returns:
        User: The user object corresponding to the given user ID, or None if no user
        with that ID exists.
    """
    print(f"typeof user_id: {type(user_id)}")
    return User.query.get(int(user_id))


@blueprint.route("/")
def index():
    """ Route for the index page.

    Returns:
        Response: The rendered "index.html" template with the current user context.
    """
    return render_template("index.html", user=current_user)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    """ Route for the login page.

    POST requests will attempt to authenticate the user with the given username
    and password.

    Returns:
        Response: The rendered "login.html" template with a success.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        bcrypt: Bcrypt = current_app.extensions["bcrypt"]
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("ログインに成功しました", "success")
            return redirect(url_for("watsxn_base.index"))
        else:
            flash("ユーザー名またはパスワードが正しくありません", "danger")
    return render_template("login.html", user=current_user)


@blueprint.route("/logout")
@login_required
def logout():
    """ Route for logging out the current user.

    Returns:
        Response: A redirect to the index page with a success message.
    """
    logout_user()
    flash("ログアウトしました", "success")
    return redirect(url_for("watsxn_base.index"))

@blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    """ Route for the signup page.

    POST requests will attempt to create a new user with the given username and password.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first() is None:
            bcrypt: Bcrypt = current_app.extensions["bcrypt"]
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            User.create(username=username, password=hashed_password)

            flash("ユーザー登録が完了しました", "success")
            return redirect(url_for("watsxn_base.login"))

        flash("このユーザー名は既に使用されています", "danger")

    return render_template("signup.html", user=current_user)
