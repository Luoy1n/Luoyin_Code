import pytest


@pytest.fixture(params=[1, 2, 3], ids=["r1", "r2", "r3"])
def login1(request):
    data = request.params
    print(request.params)
    print("获取测试数据")
    return data


def test_case1(login1):
    print("测试用例1")
