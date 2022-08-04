import pytest
import numpy as np

from modules.dummy_functions import dummy_multiplication


@pytest.mark.mark1
def test_dummy_multiplication():
    # NOTE: Typically the expected value is the first one
    assert 4.0 == dummy_multiplication(2.0, 2.0)
    assert 8.0 == dummy_multiplication(2.0, 4.0)


@pytest.mark.mark1
def test_simple_assertions():
    assert 2 == 2
    assert 2*2 == 4
    assert isinstance(2.0, float)

    my_list = [3, 2, 1]
    my_list.sort()
    assert [1, 2, 3] == my_list

    assert 'Karol' == ''.join(['K', 'a', 'r', 'o', 'l'])
    assert 5 == len('Karol')


@pytest.mark.mark1
@pytest.mark.mark2
def test_advanced_assertions():
    # NOTE: Default epsilon is ± 2.3e-06
    assert 4.0 == pytest.approx(1.9999999999999*1.9999999999999)
    # NOTE: You can specify your own epsilon
    assert 4.0 == pytest.approx(1.9*1.9, 0.2)
    np.testing.assert_array_equal([1.1, 2.2, 3.3], [1.1, 2.2, 3.3])
    # this will fail
    # np.testing.assert_array_equal([1.1, 2.2, 3.3], [1.1, 2.2, 3.2999999999999])
    # this will not fail
    np.testing.assert_array_almost_equal([1.1, 2.2, 3.3], [1.1, 2.2, 3.2999999])
    # this will fail
    # np.testing.assert_array_almost_equal([1.1, 2.2, 3.3], [1.1, 2.2, 3.299], decimal=4)

    with pytest.raises(ZeroDivisionError):
        a = 7.0 / 0.0
