import pytest
import yaml

def getdatas():
    with open("data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myids"]
        return  [add_datas,add_ids]


def add_function(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected",getdatas()[0],
                         ids=getdatas()[1])
def test_add(a,b,expected):
    assert add_function(a,b) == expected