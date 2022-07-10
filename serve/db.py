#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: juzipi
@file: db.py
@time:2022/07/10
@description:
"""

import click
from flask import current_app
from flask.cli import with_appcontext
from utils.config import SysConfig, graph

sys_config = SysConfig()


def init_db():
    """
    init db
    :return:
    """
    with open(sys_config.RELATION_PATH, 'r', encoding='utf8') as reader:
        for line in reader:
            line = line.strip()
            splits = line.split(",")
            if len(splits) == 5:
                graph.run("merge(p: Person{family: '%s', name: '%s'})" % (splits[3], splits[0]))
                graph.run("merge(p: Person{family: '%s', name: '%s'})" % (splits[4], splits[1]))
                graph.run("match(e: Person), (cc: Person) where e.name='%s' and cc.name='%s' "
                          "create(e)-[r:%s{relation: '%s'}]->(cc) return r" %
                          (splits[0], splits[1], splits[2], splits[2]))


@click.command('init-db')
@with_appcontext
def init_db_command():
    click.echo(f"start input data to {SysConfig.NEO4J_HOST} neo4j")
    init_db()
    click.echo(f"data has been input to {SysConfig.NEO4J_HOST} neo4j")


def init_database(app):
    app.cli.add_command(init_db_command)