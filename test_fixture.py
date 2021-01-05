import pytest


@pytest.fixture()
def login():
    print("登陆操作")
    print("获取token")
    username = "tom"
    password = "123456"
    token = "token123456"
    yield [username, password, token]
    print("登出操作")


def test_case1():
    print(f"login username and password:{login}")
    print("测试用例1")


def test_case2(connectDB):
    print("测试用例2")


def test_case3(login):
    print("测试用例3")


@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")
