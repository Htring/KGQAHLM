#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: juzipi
@file: search.py
@time:2022/07/10
@description:
"""
import os

from jieba import posseg
from utils.config import graph, FAMILY_DICT, SimilarWords, PersonProfile, SysConfig

target_pos = ['nh', 'n', 'nr', 'r']


def get_profile(name: str):
    s = ''
    for unit in PersonProfile.get(name, []):
        st = "<dt class = \"basicInfo-item name\" >" + str(unit) + " \
                <dd class = \"basicInfo-item value\" >" + str(PersonProfile[name][unit]) + "</dd >"
        s += st
    return s


def convert2json(input_data: list):
    json_data = {"data": [], "links": []}
    d = []
    for record in input_data:
        d.append(record['p.name'] + "_" + record['p.family'])
        d.append(record['n.name'] + "_" + record['n.family'])
        d = list(set(d))
    name_dict, count = {}, 0
    for j in d:
        j_array = j.split("_")
        name_dict[j_array[0]] = count
        count += 1
        json_data['data'].append({"name": j_array[0],
                                  "category": FAMILY_DICT.get(j_array[1], "")})
    for record in input_data:
        json_data['links'].append({
            "source": name_dict[record['p.name']],
            "target": name_dict[record['n.name']],
            "value": record['r.relation']
        })
    return json_data


def query_name(name: str):
    cypher = "match(p)-[r]->(n:Person{name:'%s'}) return  p.name, r.relation, n.name, p.family, n.family Union all\
        match(p:Person {name:'%s'}) -[r]->(n) return p.name, r.relation, n.name, p.family, n.family" % (name, name)
    data = list(graph.run(cypher))
    return convert2json(data)


def answer_question(question: str):
    """
    问答模块
    :param question:
    :return:
    """
    data_array, target_array = [], []
    for word_pos in posseg.lcut(question):
        if word_pos.flag in target_pos:
            target_array.append(word_pos.word)
    for i in range(len(target_array) - 2):
        if i == 0:
            name = target_array[0]
        else:
            name = data_array[-1]['p.name']
        cypher = "match(p)-[r:%s{relation: '%s'}]->(n:Person{name:'%s'}) return  p.name,n.name,r.relation,p.family,n.family" % (
            SimilarWords[target_array[i + 1]], SimilarWords[target_array[i + 1]], name)
        data = list(graph.run(cypher))
        data_array.extend(data)
    if data_array:
        result = [convert2json(data_array),
                  get_profile(data_array[-1]['p.name']),
                  os.path.join(SysConfig.PEOPLE_IMAGES_DIR, data_array[-1]['p.name']) + '.jpg']
    else:
        result = [{}, "", ""]
    return result


def get_answer_profile(name: str):
    """
    人员信息模块
    :param name:
    :return:
    """
    return [get_profile(name), os.path.join(SysConfig.PEOPLE_IMAGES_DIR, name + '.jpg')]
