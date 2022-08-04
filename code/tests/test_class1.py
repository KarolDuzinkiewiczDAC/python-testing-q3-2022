from argparse import ArgumentError
import os
import pytest
from modules.class1 import Class1


@pytest.fixture
def create_class1():
    '''
    This is a test fixture - it will be executed before every test that uses it.
    '''
    c1 = Class1(os.path.join(os.path.dirname(__file__), '../../data/config.yaml'))
    return c1


@pytest.mark.mark3
def test_class1_init_1():
    c1 = Class1(os.path.join(os.path.dirname(__file__), '../../data/config.yaml'))
    assert c1 is not None


@pytest.mark.mark3
def test_class1_init_2(create_class1):
    c1 = create_class1
    assert c1 is not None


@pytest.mark.mark3
def test_class1_init_3():
    with pytest.raises(ValueError) as exc:
       _ = Class1('deadbeef')
    assert 'Invalid input argument \'config_filepath\'' in str(exc.value), 'Incorrect assertion message'


@pytest.mark.mark3
def test_class1_init_4():
    '''
    Test for private class method
    '''

    with pytest.raises(RuntimeError) as exc:
        _ = Class1(os.path.join(os.path.dirname(__file__), '../../data/config2.yaml'))
    assert 'Invalid config' in str(exc.value), 'Incorrect assertion message'


@pytest.mark.mark3
def test_class1_calculate_2nd_order_polynomial(create_class1):
    '''
    Test for class method
    '''
    c1 = create_class1
    actual = c1.calculate_2nd_order_polynomial(2)
    assert 11.0 == actual
