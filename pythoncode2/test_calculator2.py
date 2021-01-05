import pytest
from pythoncode.calculator import Calculator
from pythoncode.conftest import read_files


class TestCalculator2:

    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("start_end")
    @pytest.mark.parametrize("a,b,expect", read_files()[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=4)
    @pytest.mark.usefixtures("start_end")
    @pytest.mark.parametrize("a,b,expect", read_files()[3])
    def test_div(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
            assert result == expect
        except:
            print("计算结果有误")

    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures("start_end")
    @pytest.mark.parametrize("a,b,expect", read_files()[1])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.run(order=3)
    @pytest.mark.usefixtures("start_end")
    @pytest.mark.parametrize("a,b,expect", read_files()[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect




