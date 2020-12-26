import pytest

def setup_module():
    print("\nsetup_module:整个模块开始前只执行一次")

def teardown_module():
    print("\nteardown_module:整个模块结束后只执行一次")

def setup_function():
    print("\nsetup_function:不再类中的用例执行前")

def teardown_function():
    print("\nteardown_function:不再类中的用例执行后")

def test_three():
    print("执行了test_three")

def test_four():
        print("执行了test_four")


class TestClass():

    def setup_class(self):
        print("\nsetup_class:所有用例执行前")

    def teardown_class(self):
        print("\nteardown_class:所有用例结束执行")

    def setup_method(self):
        print("\nsetup_method:每个用例开始前执行")

    def teardown_method(self):
        print("\nteardown_method:每个用例结束执行")

    def test_one(self):
        print("执行了test_one")

    def test_two(self):
        print("执行了test_two")