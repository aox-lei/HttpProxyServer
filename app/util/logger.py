# -*- coding:utf-8 -*-
import logging
import os

class logger(object):
    def __init__(self, name):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)

    def info(self, msg):
        console_handle = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s Process:%(process)d Thread:%(thread)d %(name)s %(filename)s[line:%(lineno)d](FunctionName:%(funcName)s) %(levelname)s'+os.linesep+'%(message)s'+os.linesep)
        console_handle.setFormatter(formatter)

        # 过滤器
        _filter = logging.Filter(name='app')
        console_handle.addFilter(_filter)

        self._logger.addHandler(console_handle)
        self._logger.info(msg)

    def debug(self, msg):
        console_handle = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s Process:%(process)d Thread:%(thread)d %(name)s %(filename)s[line:%(lineno)d](FunctionName:%(funcName)s) %(levelname)s'+os.linesep+'%(message)s'+os.linesep)
        console_handle.setFormatter(formatter)

        # 过滤器
        _filter = logging.Filter(name='app')
        console_handle.addFilter(_filter)

        self._logger.addHandler(console_handle)
        self._logger.debug(msg)

    def warning(self, msg):
        console_handle = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s Process:%(process)d Thread:%(thread)d %(name)s %(filename)s[line:%(lineno)d](FunctionName:%(funcName)s) %(levelname)s'+os.linesep+'%(message)s'+os.linesep)
        console_handle.setFormatter(formatter)

        # 过滤器
        _filter = logging.Filter(name='app')
        console_handle.addFilter(_filter)

        self._logger.addHandler(console_handle)
        self._logger.warning(msg)
