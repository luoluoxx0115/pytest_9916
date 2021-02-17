#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File ：conftest.py
@Auth ： luoluo
@Time ： 2021-02-17 18:16:16
@Description：
"""

import pytest


@pytest.fixture(scope='module')
def start_end():
    print('开始计算')
    yield
    print('计算结束')

