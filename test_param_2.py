import pytest

def add_function(a,b):
    return a+b
@pytest.mark.parametrize("a",[0,1,2])
@pytest.mark.parametrize("b",[2,3,5])
def test_add(a,b):
    print("测试参数堆叠组合：a->%s,b->%s"%(a,b))