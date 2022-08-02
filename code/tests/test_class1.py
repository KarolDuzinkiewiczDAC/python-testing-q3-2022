import pytest
from modules.class1 import Class1


@pytest.mark.mark1
def test_class1_init():
    c1 = Class1()
    assert c1 is not None
