#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: juzipi
@file: config.py
@time:2022/07/09
@description:
"""
import json
from py2neo import Graph
from configparser import ConfigParser

FAMILY_DICT = {"贾家荣国府": 0, "贾家宁国府": 1, "王家": 2, "史家": 3, "薛家": 4, "其他": 5, "林家": 6}

SimilarWords = {
    "爸爸": "父亲",
    "妈妈": "母亲",
    "爸": "父亲",
    "妈": "母亲",
    "父亲": "父亲",
    "母亲": "母亲",
    "儿子": "儿子",
    "女儿": "女儿",
    "丫环": "丫环",
    "兄弟": "兄弟",
    "妻": "妻",
    "老婆": "妻",
    "哥哥": "哥哥",
    "表妹": "表兄妹",
    "弟弟": "弟弟",
    "妾": "妾",
    "养父": "养父",
    "姐姐": "姐姐",
    "娘": "母亲",
    "爹": "父亲",
    "father": "父亲",
    "mother": "母亲",
    "朋友": "朋友",
    "爷爷": "爷爷",
    "奶奶": "奶奶",
    "孙子": "孙子",
    "老公": "丈夫",
    '岳母': '岳母',
    "表兄妹": "表兄妹",
    "孙女": "孙女",
    "嫂子": "嫂子",
    "暧昧": "暧昧"
}


class SysConfig(object):
    __doc__ = """ system config """

    # 单例，全局唯一
    def __new__(cls, *args, **kwargs):
        if not hasattr(SysConfig, '_instance'):
            SysConfig._instance = object.__new__(cls)
        return SysConfig._instance

    config_parser = ConfigParser()
    config_parser.read("./data/config.ini")

    NEO4J_HOST = config_parser.get("neo4j", 'host')
    NEO4J_PORT = int(config_parser.get("neo4j", 'port'))
    NEO4J_USER = config_parser.get("neo4j", 'user')
    NEO4J_PASSWORD = config_parser.get('neo4j', 'password')
    RELATION_PATH = config_parser.get('sys', 'relation_path')
    PEOPLE_IMAGES_DIR = config_parser.get('sys', 'people_images_dir')
    PEOPLE_PROFILE_FILE_PATH = config_parser.get('sys', 'people_profile_file_path')


def load_profile_dict():
    with open(SysConfig.PEOPLE_PROFILE_FILE_PATH, 'r', encoding='utf8') as reader:
        person_profile_dict = json.load(reader)
    return person_profile_dict


graph = Graph(SysConfig.NEO4J_HOST + ":" + str(SysConfig.NEO4J_PORT),
              user=SysConfig.NEO4J_USER,
              password=SysConfig.NEO4J_PASSWORD)

PersonProfile: dict = load_profile_dict()
