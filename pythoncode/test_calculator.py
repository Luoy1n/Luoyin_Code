import pytest
import yaml
from  pythoncode.calculator import Calculator


def setup_module():
    print("\n测试用例开始执行")

def teardown_module():
    print("\n测试用例执行完成")

def read_files():
    with open("./calculator_data.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        return [add_datas, sub_datas, mul_datas, div_datas]

class TestCalculator:

    def setup_class(self):
        self.calc = Calculator()
        print("\n类用例开始执行")

    def teardown_class(self):
        print("\n类用例执行完成")

    def setup(self):
        print("\n【开始计算】")

    def teardown(self):
        print("\n【计算结束】")

    def setup_class(self):
        self.calc = Calculator()
    @pytest.mark.parametrize("a,b,expect", read_files()[0])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert  result == expect

    @pytest.mark.parametrize("a,b,expect", read_files()[1])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        assert  result == expect

    @pytest.mark.parametrize("a,b,expect", read_files()[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", read_files()[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect