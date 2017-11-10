# -*- coding:utf-8 -*-
import logging
import os
from datetime import datetime
from pymongo import MongoClient
from app.util.config import config


class init(object):
    _init = {}

    def __init__(self, env='local'):
        if env == '' and 'env' in self._init:
            env = self._init.get('env')

        self._init_config(env)
        self._init_mongo()

    def _init_config(self, env):
        config(env)

    def _init_logging(self):
        console_handle = logging.StreamHandler()
        console_handle.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s %(name)s %(filename)s[line:%(lineno)d](FunctionName:%(funcName)s) %(levelname)s'+os.linesep+'%(message)s'+os.linesep)
        console_handle.setFormatter(formatter)

        # 过滤器
        filter = logging.Filter(name='app')
        console_handle.addFilter(filter)

        logging.getLogger().addHandler(console_handle)


    def _init_mongo(self):
        if 'db' not in self._init:
            client = MongoClient(config().mongo_dsn, connect=False)
            self._init['db'] = client[config().mongo_db]

    def __getattr__(self, key):
        if key in self._init:
            return self._init.get(key)
        return None
