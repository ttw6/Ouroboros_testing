# this is our unit testing for assignment 04

import pytest


def test_sum():
    from Assignment04 import return_sum
    test1 = return_sum([1, 3, 5, 7, 9])
    test2 = return_sum([-2, -5, -6, -1])
    test3 = return_sum([4, -6, 9, -1])
    test4 = return_sum([2.2, 5.1, 9.1, 1.2])
    test5 = return_sum([-1.1, -5.2, -1.4, -3.8])
    test6 = return_sum([-1.1, 2.2, -3.1])
    assert test1 == 25
    assert test2 == -14
    assert test3 == 6
    assert test4 == pytest.approx(17.6)
    assert test5 == pytest.approx(-11.5)
    assert test6 == pytest.approx(-2)
    with pytest.raises(TypeError):
        return_sum(['hello', 'hi'])
    with pytest.raises(ValueError):
        return_sum([])


# Second function
def test_return_min_max():
    from Assignment04 import return_min_max
    test_input_list = ([-1, 5, 8, 100], [5, -8, 9, 45, 88, 34, 65],
                       [-5, 8.234, -99023, 342, 9.452])
    test_output_values = ((100, -1), (88, -8), (342, -99023))

    for count, elem in enumerate(test_input_list):
        min_max_output = return_min_max(elem)
        assert min_max_output == test_output_values[count]
        assert isinstance(min_max_output, tuple)  # should be true


def test_return_min_max_exceptions():
    from Assignment04 import return_min_max
    with pytest.raises(TypeError):
        return_min_max(['string', 'why'])
    with pytest.raises(ValueError):
        return_min_max([])


def test_max_diff():
    from Assignment04 import return_max_difference
    test_input_list = [[10, 8, 5, 17, 16], [2, -7, 1.5]]
    test_output_value = [12, 9]
    for n, t in enumerate(test_input_list):
        test_output = return_max_difference(t)
        assert test_output == test_output_value[n]

    with pytest.raises(ImportError):  # Test ImportError?
        import scipy
    with pytest.raises(TypeError):  # Type error when None inputted
        return_max_difference()
        return_max_difference(['sing'])
    with pytest.raises(ValueError):  # ValueError can occur when only 1 # given
        max([])  # This is where it fails in return_max_difference
