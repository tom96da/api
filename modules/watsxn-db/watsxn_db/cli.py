# -*- coding: utf-8 -*-
#
# This flie is part of the Watsxn DB Flask extension.
# (C) 2024 tom96da.com

""" watsxn_db.cli module

This module contains the CLI commands for the Watsxn DB extension.
"""

import click
import psycopg2
from psycopg2 import sql
from flask import current_app
from flask.cli import with_appcontext

from . import config
from .shared import db

def init_db():
    for k, v in config.__dict__.items():
        if k.startswith("SQLALCHEMY_"):
            current_app.config.setdefault(k, v)

    db_params = current_app.config.get("WATSXN_DB_PARAMS")
    db_name = current_app.config.get("SQLALCHEMY_DATABASE_URI").rsplit('/', 1)[-1]

    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
    exists = cur.fetchone()
    if not exists:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        current_app.logger.info(f"Database {db_name} created")

    cur.close()
    conn.close()

    with current_app.app_context():
        db.create_all()
        current_app.logger.info("All tables created")

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Initialize the database."""
    init_db()
    click.echo("Initialized the database.")

def drop_db():
    for k, v in config.__dict__.items():
        if k.startswith("SQLALCHEMY_"):
            current_app.config.setdefault(k, v)

    db_params = current_app.config.get("WATSXN_DB_PARAMS")
    db_name = current_app.config.get("SQLALCHEMY_DATABASE_URI").rsplit('/', 1)[-1]

    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = %s AND pid <> pg_backend_pid();", (db_name,))
    cur.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(db_name)))
    current_app.logger.info(f"Database {db_name} dropped")

    cur.close()
    conn.close()

@click.command("drop-db")
@with_appcontext
def drop_db_command():
    """Drop the database."""
    drop_db()
    click.echo("Dropped the database.")

def register_db_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)
