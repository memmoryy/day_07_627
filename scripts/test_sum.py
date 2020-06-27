import os

import pytest
import yaml
from Base.getData import GetData

def sum_data():
    sum_list = []
    data = GetData.get_yaml_data("sum.yaml")
    for i in data.values():
        sum_list.append((i.get("a"),i.get("b"),i.get("c")))
    return sum_list

class TestSum:
    @pytest.mark.parametrize("a,b,c", sum_data())
    def test_sum(self, a, b, c):
        """判断两个数之和 等于 第三个数"""
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c