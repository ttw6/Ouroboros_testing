import pytest
import numpy as np


def test_sum():
    from mylist import MyList
    list1 = MyList([1, 3, 5, 7, 9])
    list2 = MyList([-2, -5, -6, -1])
    list3 = MyList([4, -6, 9, -1])
    list4 = MyList([2.2, 5.1, 9.1, 1.2])
    list5 = MyList([-1.1, -5.2, -1.4, -3.8])
    list6 = MyList([-1.1, 2.2, -3.1])
    assert list1.output_sum == 25
    assert list2.output_sum == -14
    assert list3.output_sum == 6
    assert list4.output_sum == pytest.approx(17.6)
    assert list5.output_sum == pytest.approx(-11.5)
    assert list6.output_sum == pytest.approx(-2)
    with pytest.raises(TypeError):
        np.sum(['hello', 'hi'])
    with pytest.raises(ValueError):
        MyList([])


def test_min_max():
    from mylist import MyList
    test_input_list = [[-1, 5, 8, 100], [5, -8, 9, 45, 88, 34, 65], [-5, 8.234, -99023, 342, 9.452]]
    test_output_values = ((100, -1), (88, -8), (342, -99023))

    for count, elem in enumerate(test_input_list):  # enuerate itirate and gives the index
        test = MyList(test_input_list[count])
        assert test.output_min_max == test_output_values[count]
        assert isinstance(test.output_min_max, tuple) == True

    with pytest.raises(TypeError):
        MyList(['string', 'why'])
    with pytest.raises(ValueError):
        MyList([])


def test_max_diff():
    from mylist import MyList
    test_input_list = [[10, 8, 5, 17, 16], [2, -7, 1.5]]
    test_output_value = [12, 9]
    for n, t in enumerate(test_input_list):
        test = MyList(test_input_list[n])
        assert test.output_max_diff == test_output_value[n]

    with pytest.raises(ImportError):  # Test ImportError?
        import scipy
    with pytest.raises(TypeError):  # Type error when None inputted
        MyList()
        MyList(['sing'])
    with pytest.raises(ValueError):  # ValueError can occur when only 1 number given
        max([])  # This is where it fails in return_max_difference

