# This is our first assignment as a group
import numpy as np


def main():
    input_list = [2, -7, 1.5]
    max_val = return_max_difference(input_list)
    print('Max diff = {} '.format(max_val))


def return_sum():
    pass


def return_min_max():
    pass


def return_max_difference(input_list):
    input_list = np.array(input_list)
    diffs = abs(np.diff(input_list))
    max_val = max(diffs)

    return max_val


if __name__ == "__main__":
    main()

