#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: juzipi
@file: search.py
@time:2022/07/10
@description:
"""
from KGQA import search
from flask import Blueprint, jsonify

bp = Blueprint('search', __name__)


@bp.route("/search_name/<string:name>")
def search_name(name):
    json_data = search.query_name(name)
    return jsonify(json_data)


@bp.route("/KGQA_answer/<string:question>")
def KGQA_answer(question: str):
    json_data = search.answer_question(question)
    return jsonify(json_data)


@bp.route("/get_profile/<string:name>")
def get_profile(name: str):
    return jsonify(search.get_answer_profile(name))
