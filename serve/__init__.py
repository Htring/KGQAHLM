#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: juzipi
@file: __init__.py.py
@time:2022/07/09
@description:
"""
import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'hlm_kgqa.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")

    @app.route("/search")
    def search():
        return render_template("search.html")

    @app.route("/get_all_relation")
    def get_all_relation():
        return render_template("relation.html")

    @app.route("/KGQA")
    def KGQA():
        return render_template('kgqa.html')

    from . import search
    app.register_blueprint(search.bp)

    from . import db
    db.init_database(app)

    return app


