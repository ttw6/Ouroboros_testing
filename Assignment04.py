# This is our first assignment as a group
import numpy as np
import logging


def main():
    my_list = [2, -7, 1.5]  # Example
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
    # Setup log
    logging.basicConfig(filename='fn3log.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    # Function
    try:
        logging.info('Start fn')
        if any(input_list) < 0:  #included to use warning
            logging.warning('Negative values in list')
            logging.debug('Values {}'.format(input_list))
        input_list = np.array(input_list)
        diffs = abs(np.diff(input_list))
        max_val = max(diffs)

        logging.info('Max val: {}'.format(max_val))
        return max_val

    except ImportError:  # redundancy
        logging.debug('Values {}'.format(input_list))
        logging.error('ImportError: Check if numpy is in virtualenv')
        #print('Check if numpy is in virtualenv')
    except TypeError:
        logging.debug('Values {}'.format(input_list))
        logging.debug(input_list)
        logging.error('TypeError: Check if input is a list of values')
        #print('Check if input is a list of values')
    except ValueError:
        logging.debug('Values {}'.format(input_list))
        logging.error('ValueError: Add more numbers to the list')
        #print('Add more numbers to the list')


if __name__ == "__main__":
    main()
