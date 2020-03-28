import sys
import pytest

from python.calc import Calc


def setup_module():
    print("setup_module")


class TestCalc:
    @classmethod
    def setup_class(cls):
        print("setup_class")


    def setup(self):
        print("setup")
        self.calc = Calc()

    def teardown(self):
        print("teardown")

    def teardown_class(self):
        print("teardown_class")

    test_data_add = [
        (1,2,3),
        (-1,-2,-3),
        (0.1,0.2,0.3),
        (1000,2000,3000),
        (1,-1,0),
        (1,0.1,1.1),
        (0,0,0),
        (0,1,1),
        (0,-1,-1)]
    test_data_div = [
        (1,2,0.5),
        (-1,-2,0.5),
        (0.1,0.2,0.5),
        (1000,2000,0.5),
        (4,2,2),
        (-4,2,-2)]
    @pytest.mark.parametrize("a,b,result",test_data_add)
    def test_add(self,a,b,result):
        assert self.calc.add(a,b) == result

    @pytest.mark.parametrize("a,b,result",test_data_div)
    def test_div(self,a,b,result):
        assert self.calc.div(a,b) == result
    def zatest_div_exception(self):
        with pytest.raises((ZeroDivisionError)):
            self.calc.div(1,0)

if __name__ == '__main__':

    pytest.main(['-v'])


