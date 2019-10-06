import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g: #g stores data
        g.db = sqlite3.connect( #establish a connection to a file pointed at by DATABASE configuration key
            current_app.config['DATABASE'], #points to Flask app handling the request
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row #tell the connection to return rows that behave like dicts, allows accessing columns by names
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def init_db_command():
    '''clear existing data and create new tables'''
    init_db()
    click.echo('Initialized the database')

#register close_db() and init_db_command() with the app factory
def init_app(app):
    app.teardown_appcontext(close_db) #tells Flask to call close_db when cleaning after returning the response
    app.cli.add_command(init_db_command) #add a new cli command to be called with flask command

