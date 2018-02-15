# This is our first assignment as a group
import numpy as np


def main():
    return_sum(my_list)
    return_min_max(my_list)
    return_max_difference(my_list)

    
def return_min_max(my_list):
    max_min = ((max(my_list), min(my_list)))
    return max_min
    
  
def return_sum(my_list):
    sum = 0
    for elem in my_list:
        sum += elem
    return sum


def return_max_difference(input_list):
    """Function will return maximum difference between adjacent numbers.

    Function takes in the inputted list of values, splits it into two arrays to calculate the difference between
    adjacent values, takes the absolute values of the differences to disregard positioning, and then outputs the
    maximum value.

    :param input_list: List of numbers
    :return: Maximum difference
    :raises ImportError: Check if numpy is installed or virtual env is established
    :raises TypeError: Input not given as a list of values
    :raises ValueError: Can occur when only 1 number is given in the list
    """
    try:
        input_list = np.array(input_list)
        diffs = abs(np.diff(input_list))
        max_val = max(diffs)

        return max_val
    except ImportError:  # redundancy
        print('Check if numpy is in virtualenv')
    except TypeError:
        print('Check if input is a list of values')
    except ValueError:
        print('Add more numbers to the list')


if __name__ == "__main__":
    main()
