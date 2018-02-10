# this is our unit testing for assignment 04

def test_max_diff():
    from Assignment04 import return_max_difference
    test_input_list = [[10, 8, 5, 17, 16], [2, -7, 1.5]]
    test_output_value = [12, 9]
    for n, t in enumerate(test_input_list):
        test_output = return_max_difference(t)
        assert test_output == test_output_value[n]