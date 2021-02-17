#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File ：test_calc_new.py
@Auth ： luoluo
@Time ： 2021-02-17 17:46:14
@Description：课程贴：https://ceshiren.com/t/topic/9916 作业
ps：作业要求
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
"""
import calc as calc
import pytest
import yaml
from pytest_9916.calc import Calculator


# 【读取测试数据】
with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)


# 【测试计算器类】
class TestCalc(Calculator):
    # #
    # # def setup_class(self):
    # #     print('开始计算')
    # #     self.calc = Calculator()
    # #
    # # def teardown_class(self):
    # #     print('结束计算')
    #
    # @pytest.fixture()
    # def start_end(self):
    #     print('开始计算')
    #     yield
    #     print('计算结束')

    # 【测试加法】
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(
        'a, b, expect',
        datas['add']['datas'],
        ids=datas['add']['myid']
    )
    def test_add(self, start_end, a, b, expect):
        result = self.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 【测试除法】
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize(
        'a, b, expect',
        datas['div']['datas'],
        ids=datas['div']['myid']
    )
    def test_div(self, start_end, a, b, expect):
        result = self.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 【测试减法】
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(
        'a, b, expect',
        datas['sub']['datas'],
        ids=datas['sub']['myid']
    )
    def test_sub(self, start_end, a, b, expect):
        result = self.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 【测试乘法】
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(
        'a, b, expect',
        datas['mul']['datas'],
        ids=datas['mul']['myid']
    )
    def test_mul(self, start_end, a, b, expect):
        result = self.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect


