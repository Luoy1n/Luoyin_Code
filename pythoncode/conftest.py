import pytest
import os
import yaml
from pythoncode.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + "/data.yml"

@pytest.fixture(scope="module")
def start_end():
    print("\n【开始计算】")
    yield
    print("\n【计算结束】")


@pytest.fixture(scope="module")
def get_calc():
    calc = Calculator()
    return calc

def read_files():
    with open("./calculator_data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        return [add_datas, sub_datas, mul_datas, div_datas]
